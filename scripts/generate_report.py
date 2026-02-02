#!/usr/bin/env python3
import subprocess, os
from datetime import datetime, timedelta, timezone
from collections import defaultdict

def sh(cmd):
    return subprocess.check_output(cmd, text=True)

def main():
    now = datetime.now(timezone.utc)
    since = now - timedelta(days=7)
    since_iso = since.strftime("%Y-%m-%dT%H:%M:%SZ")
    today = now.strftime("%Y-%m-%d")

    raw = sh([
        "git","log",
        f"--since={since_iso}",
        "--date=short",
        "--pretty=format:COMMIT|%H|%ad|%s",
        "--numstat"
    ])

    commits = 0
    active_days = set()
    add, dele = 0, 0
    touched = set()
    ext = defaultdict(int)

    for line in raw.splitlines():
        line = line.strip()
        if not line:
            continue
        if line.startswith("COMMIT|"):
            commits += 1
            parts = line.split("|", 3)
            if len(parts) >= 3:
                active_days.add(parts[2])
            continue

        parts = line.split("\t")
        if len(parts) == 3:
            a, d, path = parts
            if a.isdigit(): add += int(a)
            if d.isdigit(): dele += int(d)
            touched.add(path)
            _, e = os.path.splitext(path.lower())
            if e: ext[e] += 1

    top_ext = sorted(ext.items(), key=lambda x: x[1], reverse=True)[:8]
    top_ext_md = "\n".join([f"- `{k}`: {v}" for k, v in top_ext]) or "- (нет данных)"

    period = f"{since.strftime('%Y-%m-%d')} → {today} (UTC)"
    md = f"""# Отчёт активности — {today}

**Период:** {period}

## Сводка
- Активные дни: **{len(active_days)}**
- Коммиты: **{commits}**
- Изменения строк: **+{add} / -{dele}**
- Затронуто файлов: **{len(touched)}**

## По типам файлов (топ)
{top_ext_md}

## Что показать преподавателю
- папка `study-log/` — подробный тайминг занятий
- папка `reports/` — авто-отчёты (генерируются GitHub Actions)
- история коммитов по датам
"""

    os.makedirs("reports", exist_ok=True)
    report_path = f"reports/{today}.md"
    with open(report_path, "w", encoding="utf-8") as f:
        f.write(md)

    # индекс отчётов
    files = sorted([x for x in os.listdir("reports") if x.endswith(".md") and x != "README.md"], reverse=True)
    idx = "# Авто-отчёты\n\nГенерируются автоматически (раз в неделю и по кнопке).\n\n## Список\n\n"
    idx += "\n".join([f"- [{fn}](./{fn})" for fn in files]) + "\n"
    with open("reports/README.md", "w", encoding="utf-8") as f:
        f.write(idx)

    print("OK:", report_path)

if __name__ == "__main__":
    main()
