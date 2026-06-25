"""
Optional bonus: makes the greeting line in README.md actually say
"Good Morning" / "Good Afternoon" / "Good Evening" / "Good Night"
based on the current time — answering the "is it possible to change"
note on your sketch.

How it's used: a GitHub Actions workflow (update-greeting.yml) runs this
file on a schedule. It edits README.md in place, between the two marker
comments, then the workflow commits the change.

Setup:
1. Put this file in the ROOT of your profile repo (same folder as README.md).
2. Put update-greeting.yml inside a folder called .github/workflows/
   (create that folder path if it doesn't exist).
3. Change TIMEZONE and NAME below to your own.
4. Commit + push. It'll run automatically on the schedule in the workflow
   file, or you can trigger it manually from the "Actions" tab on GitHub
   (click the workflow name -> "Run workflow").
"""

import re
from datetime import datetime
from zoneinfo import ZoneInfo

TIMEZONE = "Asia/Kolkata"  # change to your timezone, e.g. "America/New_York"
NAME = "Soumya"            # change to your name
README_PATH = "README.md"
START_MARKER = "<!-- GREETING:START -->"
END_MARKER = "<!-- GREETING:END -->"


def get_greeting(hour: int) -> str:
    if 5 <= hour < 12:
        return "Good Morning"
    if 12 <= hour < 17:
        return "Good Afternoon"
    if 17 <= hour < 21:
        return "Good Evening"
    return "Good Night"


def update_readme() -> None:
    with open(README_PATH, "r", encoding="utf-8") as f:
        content = f.read()

    hour = datetime.now(ZoneInfo(TIMEZONE)).hour
    greeting = get_greeting(hour)
    new_block = f"{START_MARKER}\n### 👋 {greeting}! I'm {NAME}.\n{END_MARKER}"

    pattern = re.compile(
        re.escape(START_MARKER) + r".*?" + re.escape(END_MARKER), re.DOTALL
    )

    if not pattern.search(content):
        print("Couldn't find the GREETING:START / GREETING:END markers "
              "in README.md — nothing was changed.")
        return

    content = pattern.sub(new_block, content)

    with open(README_PATH, "w", encoding="utf-8") as f:
        f.write(content)

    print(f"Greeting updated to: {greeting}")


if __name__ == "__main__":
    update_readme()
