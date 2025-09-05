import requests
from datetime import datetime

README_PATH = "README.md"
URL = "https://api.openbrewerydb.org/v1/breweries/random"

def get_brewery():
    """Open Brewery DB API에서 무작위 브루어리 가져오기"""
    response = requests.get(URL)
    if response.status_code == 200:
        data = response.json()[0]
        name = data.get("name", "N/A")
        brewery_type = data.get("brewery_type", "N/A")
        address = data.get("address_1", "N/A")
        city = data.get("city", "N/A")
        state = data.get("state", "N/A")
        website = data.get("website_url", "N/A")
        
        return name, brewery_type, f"{address}, {city}, {state}", website
    else:
        return None, None, None, None

def update_readme():
    name, btype, addr, url = get_brewery()
    now = datetime.utcnow().strftime("%Y-%m-%d %H:%M:%S (UTC)")

    readme_content = f"""
# 🍺 Brewery Recommendation

이 리포지토리는 **[Open Brewery DB API](https://www.openbrewerydb.org/)** 를 사용하여  
무작위 브루어리 정보를 자동으로 업데이트합니다. 🚀

---

## 🌟 오늘의 추천 브루어리

| 🍻 항목 | 📌 정보 |
|--------|---------|
| **브루어리 이름** | {name} |
| **유형** | {btype} |
| **주소** | {addr} |
| **웹사이트** | {url} |

---

⏳ **업데이트 시간**: `{now}`  

> ⚡ 이 페이지는 자동 업데이트 봇에 의해 관리됩니다.
"""

    with open(README_PATH, "w", encoding="utf-8") as f:
        f.write(readme_content.strip())

if __name__ == "__main__":
    update_readme()
