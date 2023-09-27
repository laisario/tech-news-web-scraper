import requests
import time
from bs4 import BeautifulSoup
from tech_news.database import create_news


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
    news_pages_url = []
    for post in posts:
        news_pages_url.append(post["href"])
    return news_pages_url


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
    return {
        "url": soup.find("link", rel="canonical")["href"],
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
    URL_BASE = "https://blog.betrybe.com/"
    next_page_number = 1
    reportagens = []
    while len(reportagens) < amount:
        if next_page_number == 1:
            next_page_url = URL_BASE
        else:
            next_page_url = f"{URL_BASE}page/{next_page_number}/"

        html_content = fetch(next_page_url)
        urls = scrape_updates(html_content=html_content)
        for url in urls:
            page_html = fetch(url)
            new = scrape_news(page_html)
            reportagens.append(new)

            if len(reportagens) == amount:
                break

        next_page_number += 1
    create_news(reportagens[:amount])
    return reportagens[:amount]
