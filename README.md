## 현재 추천 브루어리
> {brewery_info}

⏳ 업데이트 시간: {now} (UTC)

---
자동 업데이트 봇에 의해 관리됩니다.
"""

    with open(README_PATH, "w", encoding="utf-8") as file:
        file.write(readme_content.strip())

if __name__ == "__main__":
    update_readme()