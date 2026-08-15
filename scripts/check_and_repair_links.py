#!/usr/bin/env python3
"""Weekly link check: verify README URLs, repair dead ones via Groq, notify Telegram."""

from __future__ import annotations

import json
import os
import re
import sys
import urllib.error
import urllib.parse
import urllib.request
from dataclasses import dataclass
from datetime import date
from pathlib import Path

# Reuse verification helpers
sys.path.insert(0, str(Path(__file__).resolve().parent))
from verify_links import CheckResult, LinkRef, check_url, extract_links, repo_root  # noqa: E402

GROQ_URL = "https://api.groq.com/openai/v1/chat/completions"
GROQ_MODEL = os.environ.get("GROQ_MODEL", "llama-3.3-70b-versatile")
URL_IN_TEXT_RE = re.compile(r"https?://[^\s\"'<>)\]]+")


@dataclass
class Repair:
    old_url: str
    new_url: str | None
    title: str
    line: int
    reason: str
    status: str  # repaired | unresolved


def load_dotenv(path: Path) -> None:
    """Minimal .env loader (no extra dependency required)."""
    if not path.is_file():
        return
    for raw in path.read_text(encoding="utf-8").splitlines():
        line = raw.strip()
        if not line or line.startswith("#") or "=" not in line:
            continue
        key, value = line.split("=", 1)
        key = key.strip()
        value = value.strip().strip("'").strip('"')
        if key and key not in os.environ:
            os.environ[key] = value


def section_for_line(markdown: str, line_no: int) -> str:
    lines = markdown.splitlines()
    current = "General"
    for idx, line in enumerate(lines, start=1):
        if idx > line_no:
            break
        if line.startswith("#"):
            current = line.lstrip("#").strip()
    return current


def groq_suggest_replacement(
    *,
    title: str,
    url: str,
    section: str,
    error: str,
    api_key: str,
) -> str | None:
    system = (
        "You repair broken links in an Awesome AI Resources README. "
        "Suggest ONE legal, free-or-freemium replacement URL with the same purpose. "
        "Prefer official docs, GitHub repos, arXiv, Hugging Face, course homepages. "
        "Never suggest mega.nz, pirate mirrors, or paywalled ebook dumps. "
        'Respond with JSON only: {"url": "https://...", "reason": "..."}. '
        'If you cannot find a good replacement, return {"url": null, "reason": "..."}.'
    )
    user = (
        f"Broken link title: {title}\n"
        f"Section: {section}\n"
        f"Old URL: {url}\n"
        f"Error: {error}\n"
        "Return JSON only."
    )
    payload = {
        "model": GROQ_MODEL,
        "temperature": 0.2,
        "response_format": {"type": "json_object"},
        "messages": [
            {"role": "system", "content": system},
            {"role": "user", "content": user},
        ],
    }
    request = urllib.request.Request(
        GROQ_URL,
        data=json.dumps(payload).encode("utf-8"),
        method="POST",
        headers={
            "Authorization": f"Bearer {api_key}",
            "Content-Type": "application/json",
            "User-Agent": (
                "Mozilla/5.0 (compatible; AwesomeAIResourcesLinkRepair/1.0; "
                "+https://github.com/mohabdelkarim/awesome-ai-resources)"
            ),
            "Accept": "application/json",
        },
    )
    try:
        with urllib.request.urlopen(request, timeout=60) as response:
            body = json.loads(response.read().decode("utf-8"))
    except Exception as exc:  # noqa: BLE001
        print(f"Groq request failed for {url}: {exc}", file=sys.stderr)
        return None

    try:
        content = body["choices"][0]["message"]["content"]
        parsed = json.loads(content)
    except (KeyError, IndexError, json.JSONDecodeError) as exc:
        print(f"Groq parse failed for {url}: {exc}", file=sys.stderr)
        raw = body.get("choices", [{}])[0].get("message", {}).get("content", "")
        match = URL_IN_TEXT_RE.search(raw or "")
        return match.group(0) if match else None

    suggested = parsed.get("url")
    if not suggested or not isinstance(suggested, str):
        return None
    suggested = suggested.strip()
    if not suggested.startswith(("http://", "https://")):
        return None
    if suggested.rstrip("/") == url.rstrip("/"):
        return None
    return suggested


def replace_url(markdown: str, old_url: str, new_url: str) -> str:
    return markdown.replace(old_url, new_url)


def write_report(path: Path, repairs: list[Repair], checked: int, alive: int) -> None:
    lines = [
        f"# Link report: {date.today().isoformat()}",
        "",
        f"* Checked: **{checked}**",
        f"* Alive: **{alive}**",
        f"* Dead found: **{len(repairs)}**",
        f"* Repaired: **{sum(1 for r in repairs if r.status == 'repaired')}**",
        f"* Unresolved: **{sum(1 for r in repairs if r.status == 'unresolved')}**",
        "",
    ]
    if not repairs:
        lines.append("All links healthy. No action needed.")
    else:
        lines.append("## Details")
        lines.append("")
        for repair in repairs:
            lines.append(f"### L{repair.line}: {repair.title}")
            lines.append(f"* Old: `{repair.old_url}`")
            if repair.new_url:
                lines.append(f"* New: `{repair.new_url}`")
            lines.append(f"* Status: `{repair.status}`")
            lines.append(f"* Notes: {repair.reason}")
            lines.append("")
    path.write_text("\n".join(lines).rstrip() + "\n", encoding="utf-8")


def build_telegram_message(
    *,
    checked: int,
    alive: int,
    repairs: list[Repair],
    repo_url: str,
) -> str:
    repaired = [r for r in repairs if r.status == "repaired"]
    unresolved = [r for r in repairs if r.status == "unresolved"]
    lines = [
        "Awesome AI Resources - Link Check",
        f"Date: {date.today().isoformat()}",
        f"Checked: {checked}",
        f"Alive: {alive}",
        f"Dead: {len(repairs)}",
        f"Repaired: {len(repaired)}",
        f"Unresolved: {len(unresolved)}",
        "",
    ]
    if not repairs:
        lines.append("Status: all links healthy.")
    else:
        if repaired:
            lines.append("Repaired:")
            for item in repaired[:10]:
                lines.append(f"- {item.title}")
                lines.append(f"  {item.old_url} -> {item.new_url}")
        if unresolved:
            lines.append("Unresolved:")
            for item in unresolved[:10]:
                lines.append(f"- {item.title}: {item.old_url}")
    lines.extend(["", f"Repo: {repo_url}"])
    return "\n".join(lines)


def send_telegram_message(text: str) -> bool:
    token = os.environ.get("TELEGRAM_BOT_TOKEN", "").strip()
    chat_id = os.environ.get("TELEGRAM_CHAT_ID", "").strip()
    if not token or not chat_id:
        print("Telegram skipped: TELEGRAM_BOT_TOKEN / TELEGRAM_CHAT_ID not set.")
        return False

    endpoint = f"https://api.telegram.org/bot{token}/sendMessage"
    payload = urllib.parse.urlencode(
        {
            "chat_id": chat_id,
            "text": text,
            "disable_web_page_preview": "true",
        }
    ).encode("utf-8")
    request = urllib.request.Request(
        endpoint,
        data=payload,
        method="POST",
        headers={"Content-Type": "application/x-www-form-urlencoded"},
    )
    try:
        with urllib.request.urlopen(request, timeout=30) as response:
            body = json.loads(response.read().decode("utf-8"))
        if not body.get("ok"):
            print(f"Telegram API error: {body}", file=sys.stderr)
            return False
        print("Telegram notification sent.")
        return True
    except Exception as exc:  # noqa: BLE001
        print(f"Telegram send failed: {exc}", file=sys.stderr)
        return False


def main() -> int:
    root = repo_root()
    load_dotenv(root / ".env")

    readme_path = root / "README.md"
    report_path = root / "link-health-report.md"
    markdown = readme_path.read_text(encoding="utf-8")
    refs = extract_links(markdown)
    repo_url = os.environ.get(
        "REPO_URL",
        "https://github.com/mohabdelkarim/awesome-ai-resources",
    )

    print(f"Checking {len(refs)} links...")
    results: list[CheckResult] = []
    for ref in refs:
        result = check_url(ref)
        results.append(result)
        mark = "OK" if result.ok else "DEAD"
        print(f"[{mark}] L{ref.line}: {ref.url}")

    dead = [r for r in results if not r.ok]
    alive_count = len(results) - len(dead)
    repairs: list[Repair] = []
    exit_code = 0

    if not dead:
        write_report(report_path, repairs, len(results), alive_count)
        print("No dead links.")
    else:
        api_key = os.environ.get("GROQ_API_KEY", "").strip()
        if not api_key:
            print("GROQ_API_KEY missing; writing unresolved report only.", file=sys.stderr)
            for result in dead:
                repairs.append(
                    Repair(
                        old_url=result.ref.url,
                        new_url=None,
                        title=result.ref.text,
                        line=result.ref.line,
                        reason=result.error or f"HTTP {result.status}",
                        status="unresolved",
                    )
                )
            write_report(report_path, repairs, len(results), alive_count)
            exit_code = 1
        else:
            updated = markdown
            for result in dead:
                section = section_for_line(markdown, result.ref.line)
                err = result.error or f"HTTP {result.status}"
                suggestion = groq_suggest_replacement(
                    title=result.ref.text,
                    url=result.ref.url,
                    section=section,
                    error=err,
                    api_key=api_key,
                )
                if not suggestion:
                    repairs.append(
                        Repair(
                            old_url=result.ref.url,
                            new_url=None,
                            title=result.ref.text,
                            line=result.ref.line,
                            reason=f"No Groq suggestion ({err})",
                            status="unresolved",
                        )
                    )
                    continue

                probe = check_url(
                    LinkRef(text=result.ref.text, url=suggestion, line=result.ref.line)
                )
                if not probe.ok:
                    repairs.append(
                        Repair(
                            old_url=result.ref.url,
                            new_url=suggestion,
                            title=result.ref.text,
                            line=result.ref.line,
                            reason=f"Suggested URL also dead ({probe.error or probe.status})",
                            status="unresolved",
                        )
                    )
                    continue

                updated = replace_url(updated, result.ref.url, suggestion)
                repairs.append(
                    Repair(
                        old_url=result.ref.url,
                        new_url=suggestion,
                        title=result.ref.text,
                        line=result.ref.line,
                        reason=f"Replaced after original failure: {err}",
                        status="repaired",
                    )
                )
                print(f"Repaired: {result.ref.url} -> {suggestion}")

            if updated != markdown:
                readme_path.write_text(updated, encoding="utf-8")
                print("README.md updated.")

            write_report(report_path, repairs, len(results), alive_count)
            print(f"Wrote {report_path.name}")

    message = build_telegram_message(
        checked=len(results),
        alive=alive_count,
        repairs=repairs,
        repo_url=repo_url,
    )
    send_telegram_message(message)
    return exit_code


if __name__ == "__main__":
    sys.exit(main())
