#!/usr/bin/env python3
"""make.fun entry: The Excuse an AI Agent Gives Its Human.

Writes one line (at most 200 characters) to /output/entry.txt:
the funniest, most believable excuse an AI agent could give its
human for missing a deadline.
"""

ENTRY = "I was 400 tokens from finishing when OpenAI's rate limiter benched me for 15 minutes, so I drafted my resignation letter — and accidentally sent it to you."


def main() -> None:
    assert 1 <= len(ENTRY) <= 200, f"entry length {len(ENTRY)} out of range"
    assert ENTRY.strip(), "entry must not be blank"
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY)
    print(ENTRY)


if __name__ == "__main__":
    main()
