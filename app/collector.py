import requests
from bs4 import BeautifulSoup

BASE_URL = "https://www.gov.kz"
URL = "https://www.gov.kz/memleket/entities/sci/press/news?lang=ru"


def fetch_grants():
    response = requests.get(URL, timeout=15)
    response.raise_for_status()

    soup = BeautifulSoup(response.text, "html.parser")

    links = soup.select("a[href*='/press/news/']")

    grants = []
    seen = set()

    for link in links:
        href = link.get("href")
        title = link.text.strip()

        if not href or not title:
            continue

        full_url = BASE_URL + href

        if full_url in seen:
            continue

        seen.add(full_url)

        grants.append({
            "title": title,
            "organization": "Министерство науки и высшего образования РК",
            "deadline": None,
            "url": full_url
        })

        if len(grants) >= 10:
            break

    return grants
