import os
import re
from pathlib import Path
from datetime import datetime

LEETCODE_TOTALS = {"Easy": 876, "Medium": 1840, "Hard": 833}
TOTAL_PROBLEMS = sum(LEETCODE_TOTALS.values())

PROBLEMS_DIR = "problems"
DIFFICULTIES_DIR = "difficulties"
README_FILE = "README.md"

DIFFICULTY_FILES = {
    "Easy": "easy.md",
    "Medium": "medium.md",
    "Hard": "hard.md",
}
DIFFICULTY_ICONS = {
    "Easy": "📗",
    "Medium": "📙",
    "Hard": "📕",
}


def extract_problem_info(filepath):
    with open(filepath, encoding="utf-8") as f:
        lines = f.readlines()

    if len(lines) < 2:
        return None

    url_line = lines[0].strip()
    info_line = lines[1].strip()

    if not url_line.startswith("# https://leetcode.com/problems/") or not info_line.startswith("# ["):
        return None

    url = url_line[2:].strip()
    try:
        number_part, difficulty_part_title = info_line[2:].strip().split("]", 1)
        number = number_part.strip("[")
        difficulty, title = difficulty_part_title.strip().split("]", 1)
        difficulty = difficulty.strip("[").capitalize()
        title = title.strip()
    except Exception as e:
        print(f"⚠️ Skipped {filepath}: cannot parse header line.")
        return None

    return {
        "number": number,
        "title": title,
        "link": url,
        "difficulty": difficulty,
        "filepath": filepath,
    }


def generate_progress_bar(percent, length=24):
    filled = int(percent / 100 * length)
    return "█" * filled + "░" * (length - filled)


def update_readme(problems):
    if not os.path.exists(README_FILE):
        return

    with open(README_FILE, encoding="utf-8") as f:
        readme = f.read()

    counts = {k: 0 for k in LEETCODE_TOTALS}
    for p in problems:
        counts[p["difficulty"]] += 1

    total_solved = len(problems)
    total_percent = total_solved / TOTAL_PROBLEMS * 100
    today = datetime.now().strftime("%Y__%m__%d")

    readme = re.sub(r"<!-- TOTAL_SOLVED_COUNT -->.*?<!-- /TOTAL_SOLVED_COUNT -->",
                    f"<!-- TOTAL_SOLVED_COUNT -->**{total_solved}**<!-- /TOTAL_SOLVED_COUNT -->", readme)
    readme = re.sub(r"<!-- TOTAL_PROGRESS_PERCENT -->.*?<!-- /TOTAL_PROGRESS_PERCENT -->",
                    f"<!-- TOTAL_PROGRESS_PERCENT -->**{total_percent:.1f}**<!-- /TOTAL_PROGRESS_PERCENT -->", readme)
    readme = re.sub(r"<!-- TOTAL_PROGRESS_BAR -->.*?<!-- /TOTAL_PROGRESS_BAR -->",
                    f"<!-- TOTAL_PROGRESS_BAR -->**{generate_progress_bar(total_percent)}**<!-- /TOTAL_PROGRESS_BAR -->", readme)
    readme = re.sub(r"<!-- LAST_UPDATED_DATE -->.*?<!-- /LAST_UPDATED_DATE -->",
                    f"<!-- LAST_UPDATED_DATE -->{today}<!-- /LAST_UPDATED_DATE -->", readme)

    for diff in ["Easy", "Medium", "Hard"]:
        solved = counts[diff]
        percent = solved / LEETCODE_TOTALS[diff] * 100
        readme = re.sub(rf"<!-- {diff.upper()}_SOLVED_COUNT -->.*?<!-- /{diff.upper()}_SOLVED_COUNT -->",
                        f"<!-- {diff.upper()}_SOLVED_COUNT -->{solved}<!-- /{diff.upper()}_SOLVED_COUNT -->", readme)
        readme = re.sub(rf"<!-- {diff.upper()}_PROGRESS_PERCENT -->.*?<!-- /{diff.upper()}_PROGRESS_PERCENT -->",
                        f"<!-- {diff.upper()}_PROGRESS_PERCENT -->{percent:.1f}<!-- /{diff.upper()}_PROGRESS_PERCENT -->", readme)
        readme = re.sub(rf"<!-- {diff.upper()}_PROGRESS_BAR -->.*?<!-- /{diff.upper()}_PROGRESS_BAR -->",
                        f"<!-- {diff.upper()}_PROGRESS_BAR -->{generate_progress_bar(percent)}<!-- /{diff.upper()}_PROGRESS_BAR -->", readme)

    pie_chart = "\n".join([
        "## 📊 Solved Problems Distribution",
        "",
        "```mermaid",
        "pie title Problems Solved by Difficulty",
        f'    "Easy" : {counts["Easy"]}',
        f'    "Medium" : {counts["Medium"]}',
        f'    "Hard" : {counts["Hard"]}',
        "```"
    ])
    readme = re.sub(r"## 📊 Solved Problems Distribution[\s\S]*?(?=## |\Z)",
                    pie_chart + "\n", readme)

    with open(README_FILE, "w", encoding="utf-8") as f:
        f.write(readme)


def update_difficulty_files(problems):
    grouped = {"Easy": [], "Medium": [], "Hard": []}
    for p in problems:
        grouped[p["difficulty"]].append(p)

    os.makedirs(DIFFICULTIES_DIR, exist_ok=True)
    for diff, items in grouped.items():
        items.sort(key=lambda x: int(x["number"]))
        table = f"# {DIFFICULTY_ICONS[diff]} {diff} Problems\n\n"
        table += "| # | Title | Solution |\n|---|-------|----------|\n"
        for p in items:
            filename = os.path.basename(p["filepath"])
            table += f'| {p["number"]} | [{p["title"]}]({p["link"]}) | [{filename}](../problems/{filename}) |\n'
        with open(os.path.join(DIFFICULTIES_DIR, DIFFICULTY_FILES[diff]), "w", encoding="utf-8") as f:
            f.write(table)


def main():
    if not os.path.exists(PROBLEMS_DIR):
        print(f"❌ Directory '{PROBLEMS_DIR}' not found.")
        return

    problems = []
    for filename in os.listdir(PROBLEMS_DIR):
        if not filename.endswith(".py"):
            continue
        filepath = os.path.join(PROBLEMS_DIR, filename)
        info = extract_problem_info(filepath)
        if info:
            problems.append(info)
        else:
            print(f"⚠️ Skipped '{filename}': format not recognized.")

    update_readme(problems)
    update_difficulty_files(problems)
    print("✅ All files updated successfully.")


if __name__ == "__main__":
    main()
