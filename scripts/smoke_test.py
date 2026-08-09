#!/usr/bin/env python3
"""Smoke-test local .env wiring: link checks, Groq, Telegram."""

from __future__ import annotations

import json
import os
import sys
import urllib.parse
import urllib.request
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from check_and_repair_links import load_dotenv  # noqa: E402
from verify_links import check_url, extract_links, repo_root  # noqa: E402
from verify_links import LinkRef  # noqa: E402


def ok(label: str) -> None:
    print(f"[PASS] {label}")


def fail(label: str, detail: str) -> None:
    print(f"[FAIL] {label}: {detail}")


def main() -> int:
    root = repo_root()
    load_dotenv(root / ".env")
    failures = 0

    # 1) Link verification (sample + full count)
    readme = (root / "README.md").read_text(encoding="utf-8")
    refs = extract_links(readme)
    print(f"Found {len(refs)} links in README.md")
    sample = refs[:5]
    for ref in sample:
        result = check_url(ref)
        if result.ok:
            ok(f"sample link {ref.url}")
        else:
            fail(f"sample link {ref.url}", result.error or str(result.status))
            failures += 1

    # 2) Groq
    groq_key = os.environ.get("GROQ_API_KEY", "").strip()
    if not groq_key:
        fail("Groq", "GROQ_API_KEY empty in .env")
        failures += 1
    else:
        payload = {
            "model": os.environ.get("GROQ_MODEL", "llama-3.3-70b-versatile"),
            "messages": [{"role": "user", "content": "Reply with exactly: pong"}],
            "max_tokens": 8,
            "temperature": 0,
        }
        req = urllib.request.Request(
            "https://api.groq.com/openai/v1/chat/completions",
            data=json.dumps(payload).encode("utf-8"),
            method="POST",
            headers={
                "Authorization": f"Bearer {groq_key}",
                "Content-Type": "application/json",
                "User-Agent": (
                    "Mozilla/5.0 (compatible; AwesomeAIResourcesSmokeTest/1.0; "
                    "+https://github.com/mohabdelkarim/awesome-ai-resources)"
                ),
                "Accept": "application/json",
            },
        )
        try:
            with urllib.request.urlopen(req, timeout=45) as resp:
                body = json.loads(resp.read().decode("utf-8"))
            content = body["choices"][0]["message"]["content"]
            ok(f"Groq API ({content.strip()[:40]})")
        except Exception as exc:  # noqa: BLE001
            fail("Groq", str(exc))
            failures += 1

    # 3) Telegram
    token = os.environ.get("TELEGRAM_BOT_TOKEN", "").strip()
    chat_id = os.environ.get("TELEGRAM_CHAT_ID", "").strip()
    if not token or not chat_id:
        fail("Telegram", "TELEGRAM_BOT_TOKEN / TELEGRAM_CHAT_ID empty in .env")
        failures += 1
    else:
        text = (
            "Awesome AI Resources smoke test\n"
            "Link check Telegram wiring works.\n"
            f"Repo: {os.environ.get('REPO_URL', 'https://github.com/mohabdelkarim/awesome-ai-resources')}"
        )
        data = urllib.parse.urlencode(
            {"chat_id": chat_id, "text": text, "disable_web_page_preview": "true"}
        ).encode("utf-8")
        req = urllib.request.Request(
            f"https://api.telegram.org/bot{token}/sendMessage",
            data=data,
            method="POST",
            headers={"Content-Type": "application/x-www-form-urlencoded"},
        )
        try:
            with urllib.request.urlopen(req, timeout=30) as resp:
                body = json.loads(resp.read().decode("utf-8"))
            if body.get("ok"):
                ok("Telegram sendMessage")
            else:
                fail("Telegram", str(body))
                failures += 1
        except Exception as exc:  # noqa: BLE001
            fail("Telegram", str(exc))
            failures += 1

    # Optional: verify a known-good URL object still imports
    _ = LinkRef(text="x", url="https://example.com", line=1)

    if failures:
        print(f"\n{failures} check(s) failed. Fill .env and re-run.")
        return 1
    print("\nAll smoke checks passed.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
