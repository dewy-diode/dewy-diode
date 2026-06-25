
import re
from datetime import datetime
from zoneinfo import ZoneInfo

TIMEZONE = "Asia/Kolkata" 
NAME = "Soumya"           
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
