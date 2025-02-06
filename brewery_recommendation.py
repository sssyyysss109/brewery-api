import requests
import os
from datetime import datetime

# README 파일 경로
README_PATH = "README.md"
URL = "https://api.openbrewerydb.org/v1/breweries/random"

def get_brewery():
    """Open Brewery DB API를 호출하여 무작위 브루어리 데이터를 가져옴"""
    response = requests.get(URL)
    if response.status_code == 200:
        data = response.json()[0]  # 첫 번째 브루어리 데이터
        name = data["name"]
        brewery_type = data["brewery_type"]
        address = data["address_1"]
        city = data["city"]
        state = data["state"]
        website = data["website_url"]
        
        return (f"브루어리 이름: {name}\n"
                f"유형: {brewery_type}\n"
                f"주소: {address}, {city}, {state}\n"
                f"웹사이트: {website}")
    else:
        return "브루어리 정보를 가져오는 데 실패했습니다."

def update_readme():
    """README.md 파일을 업데이트"""
    brewery_info = get_brewery()
    now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    
    readme_content = f"""
# Brewery Recommendation

이 리포지토리는 Open Brewery DB API를 사용하여 무작위 브루어리 정보를 자동으로 업데이트합니다.

## 현재 추천 브루어리
> {brewery_info}

⏳ 업데이트 시간: {now} (UTC)

---
자동 업데이트 봇에 의해 관리됩니다.
"""

    with open(README_PATH, "w", encoding="utf-8") as file:
        file.write(readme_content)

if __name__ == "__main__":
    update_readme()