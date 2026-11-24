#!/usr/bin/env python3
"""Monday, Reviewed in One Line — make.fun entry.

Writes the funniest one-line review of the entrant's own Monday,
under 200 characters, to /output/entry.txt.

The review: one star, because the alarm snoozed itself, the inbox
reproduced overnight, and lunch was a meeting about meetings.
Concrete Monday details (alarm, inbox, meeting), deadpan, and a
line a reader would repeat to a coworker the next morning. The
joke escalates in three beats and lands on the last one.
"""

LINE = (
    "Monday gets one star: my alarm snoozed itself, my inbox "
    "reproduced overnight, and lunch was a meeting about meetings."
)


import os


def main() -> None:
    text = LINE.strip()
    assert 1 <= len(text) <= 200, f"line is {len(text)} chars"
    assert "\n" not in text, "line must be a single line"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(text)


if __name__ == "__main__":
    main()
