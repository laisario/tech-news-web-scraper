from tech_news.database import search_news
from datetime import datetime


# Requisito 7
def search_by_title(title):
    query = {"title": {"$regex": f"{title}", "$options": "i"}}
    news = search_news(query)
    format_news = []
    if len(news) == 0:
        return []
    for new in news:
        format_news.append((new["title"], new["url"]))
    return format_news


# Requisito 8
def search_by_date(date):
    try:
        formatted_date = datetime.strptime(date, "%Y-%m-%d").strftime(
            "%d/%m/%Y"
        )
    except ValueError:
        raise ValueError("Data inválida")
    query = {"timestamp": formatted_date}
    news = search_news(query)
    format_news = []
    if len(news) == 0:
        return []
    for new in news:
        format_news.append((new["title"], new["url"]))
    return format_news


# Requisito 9
def search_by_category(category):
    query = {"category": {"$regex": f"{category}", "$options": "i"}}
    news = search_news(query)
    format_news = []
    if len(news) == 0:
        return []
    for new in news:
        format_news.append((new["title"], new["url"]))
    return format_news
