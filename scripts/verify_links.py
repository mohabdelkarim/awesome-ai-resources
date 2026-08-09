#!/usr/bin/env python3
"""Extract and verify HTTP(S) links from README.md."""

from __future__ import annotations

import argparse
import concurrent.futures
import re
import ssl
import sys
import urllib.error
import urllib.request
from dataclasses import dataclass
from pathlib import Path

MARKDOWN_LINK_RE = re.compile(r"\[([^\]]+)\]\((https?://[^)\s]+)\)")
BARE_URL_RE = re.compile(r"(?<!\()(?<!\]\()https?://[^\s<>\")\]]+")
USER_AGENT = (
    "Mozilla/5.0 (compatible; AwesomeAIResourcesLinkCheck/1.0; "
    "+https://github.com/mohabdelkarim/awesome-ai-resources)"
)

# Treat rate-limits / soft blocks as "alive" (host is reachable).
SOFT_OK_STATUSES = {401, 403, 429}


def ssl_context() -> ssl.SSLContext:
    try:
        import certifi

        return ssl.create_default_context(cafile=certifi.where())
    except Exception:  # noqa: BLE001
        return ssl.create_default_context()


@dataclass(frozen=True)
class LinkRef:
    text: str
    url: str
    line: int


@dataclass
class CheckResult:
    ref: LinkRef
    ok: bool
    status: int | None
    error: str | None


def repo_root() -> Path:
    return Path(__file__).resolve().parent.parent


def extract_links(markdown: str) -> list[LinkRef]:
    refs: list[LinkRef] = []
    seen: set[tuple[str, int]] = set()
    for line_no, line in enumerate(markdown.splitlines(), start=1):
        for match in MARKDOWN_LINK_RE.finditer(line):
            key = (match.group(2), line_no)
            if key in seen:
                continue
            seen.add(key)
            refs.append(LinkRef(text=match.group(1), url=match.group(2), line=line_no))
        # Table cells and bare URLs
        stripped = MARKDOWN_LINK_RE.sub(" ", line)
        for match in BARE_URL_RE.finditer(stripped):
            url = match.group(0).rstrip(".,;")
            key = (url, line_no)
            if key in seen:
                continue
            seen.add(key)
            refs.append(LinkRef(text=url, url=url, line=line_no))
    return refs


def check_url(ref: LinkRef, timeout: float = 20.0) -> CheckResult:
    headers = {"User-Agent": USER_AGENT, "Accept": "*/*"}
    context = ssl_context()
    for method in ("HEAD", "GET"):
        request = urllib.request.Request(ref.url, method=method, headers=headers)
        try:
            with urllib.request.urlopen(request, timeout=timeout, context=context) as response:
                status = getattr(response, "status", None) or response.getcode()
                if 200 <= int(status) < 400:
                    return CheckResult(ref=ref, ok=True, status=int(status), error=None)
                # Some hosts reject HEAD; retry with GET
                if method == "HEAD" and int(status) in {403, 405, 501}:
                    continue
                return CheckResult(
                    ref=ref,
                    ok=False,
                    status=int(status),
                    error=f"HTTP {status}",
                )
        except urllib.error.HTTPError as exc:
            # Treat common anti-bot / method issues as soft pass on GET body
            if method == "HEAD" and exc.code in {403, 405, 501}:
                continue
            if exc.code in SOFT_OK_STATUSES:
                # Reachable but gated / rate-limited; count as alive
                return CheckResult(ref=ref, ok=True, status=exc.code, error=None)
            if method == "HEAD":
                continue
            return CheckResult(ref=ref, ok=False, status=exc.code, error=str(exc))
        except Exception as exc:  # noqa: BLE001 - collect any network failure
            if method == "HEAD":
                continue
            return CheckResult(ref=ref, ok=False, status=None, error=str(exc))
    return CheckResult(ref=ref, ok=False, status=None, error="unreachable")


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--readme",
        type=Path,
        default=repo_root() / "README.md",
        help="Path to README.md",
    )
    parser.add_argument("--workers", type=int, default=16)
    parser.add_argument(
        "--fail-on-dead",
        action="store_true",
        help="Exit non-zero if any link is dead",
    )
    args = parser.parse_args()

    markdown = args.readme.read_text(encoding="utf-8")
    refs = extract_links(markdown)
    print(f"Checking {len(refs)} links in {args.readme} ...")

    results: list[CheckResult] = []
    with concurrent.futures.ThreadPoolExecutor(max_workers=args.workers) as pool:
        futures = [pool.submit(check_url, ref) for ref in refs]
        for future in concurrent.futures.as_completed(futures):
            results.append(future.result())

    results.sort(key=lambda r: (r.ref.line, r.ref.url))
    dead = [r for r in results if not r.ok]
    alive = [r for r in results if r.ok]

    for result in results:
        mark = "OK " if result.ok else "DEAD"
        detail = result.status if result.status is not None else result.error
        print(f"[{mark}] L{result.ref.line}: {result.ref.url} ({detail})")

    print(f"\nAlive: {len(alive)} | Dead: {len(dead)} | Total: {len(results)}")
    if dead:
        print("\nDead links:")
        for result in dead:
            print(f"- L{result.ref.line} {result.ref.url} :: {result.error or result.status}")

    if args.fail_on_dead and dead:
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(main())
