import requests
import time
from bs4 import BeautifulSoup


# Requisito 1
def fetch(url):
    try:
        time.sleep(1)
        page = requests.get(url, headers={"user-agent": "Fake user-agent"})
        if page.status_code == 200:
            html_content = page.text
            return html_content
        else:
            return None
    except requests.ReadTimeout:
        return None


# Requisito 2
def scrape_updates(html_content):
    soup = BeautifulSoup(html_content, "html.parser")
    posts = soup.find_all("a", {"class": "cs-overlay-link"})
    news = []
    for post in posts:
        news.append(post["href"])
    return news


# Requisito 3
def scrape_next_page_link(html_content):
    try:
        soup_page = BeautifulSoup(html_content, "html.parser")
        return soup_page.find(
            "a",
            {"class": "next page-numbers"},
        )["href"]
    except TypeError:
        return None


# Requisito 4
def scrape_news(html_content):
    soup = BeautifulSoup(html_content, "html.parser")
    print(soup.find("link", rel="canonical").get("href"), "aaaaaaaaaa")
    return {
        "url": soup.find("link", rel="canonical").get("href"),
        "title": soup.find("h1", {"class": "entry-title"}).string.strip(),
        "timestamp": soup.find("li", {"class": "meta-date"}).string,
        "writer": soup.find("span", {"class": "fn"}).a.string.strip(),
        "reading_time": int(
            soup.find("li", {"class": "meta-reading-time"}).text.split()[0]
        ),
        "summary": soup.find("div", {"class": "entry-content"})
        .find("p")
        .text.strip(),
        "category": soup.find("span", {"class": "label"}).string.strip(),
    }


# Requisito 5
def get_tech_news(amount):
    """Seu código deve vir aqui"""
    raise NotImplementedError
