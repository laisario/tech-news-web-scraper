from tech_news.analyzer.reading_plan import (
    ReadingPlanService,
)  # noqa: F401, E261, E501
import pytest
from unittest.mock import patch

NEWS = [
    {
        "url": "https://blog.betrybe.com/novidades/noticia_0.htm",
        "title": "noticia_0",
        "timestamp": "23/11/2020",
        "writer": "Escritor_0",
        "reading_time": 2,
        "summary": "Sumario da noticia_0",
        "category": "Tecnologia",
    },
    {
        "url": "https://blog.betrybe.com/novidades/noticia-bacana",
        "title": "Notícia bacana 1",
        "writer": "Eu",
        "summary": "Algo muito bacana aconteceu",
        "reading_time": 4,
        "timestamp": "04/04/2021",
        "category": "Ferramentas",
    },
    {
        "url": "https://blog.betrybe.com/novidades/noticia-legal",
        "title": "Notícia bacana 2",
        "writer": "Você",
        "summary": "Algo muito bacana aconteceu de novo",
        "reading_time": 1,
        "timestamp": "07/04/2022",
        "category": "Novidades",
    },
    {
        "url": "https://blog.betrybe.com/novidades/noticia_10.htm",
        "title": "noticia_13",
        "timestamp": "23/11/2025",
        "writer": "Escritor_10",
        "reading_time": 15,
        "summary": "Sumario da noticia_10",
        "category": "Educação",
    },
]


def test_reading_plan_group_news():
    reading_plan_service = ReadingPlanService()


    expected = {
        "readable": [
            {
                "unfilled_time": 3,
                "chosen_news": [
                    (
                        "noticia_0",
                        2,
                    ),
                    (
                        "Notícia bacana 1",
                        4,
                    ),
                    (
                        "Notícia bacana 2",
                        1,
                    ),
                ],
            },
        ],
        "unreadable": [("noticia_13", 15)],
    }
    with patch("tech_news.analyzer.reading_plan.find_news") as find_news_mock:
        find_news_mock.return_value = NEWS
        result = reading_plan_service.group_news_for_available_time(10)
    assert result == expected

    with pytest.raises(
        ValueError, match="Valor 'available_time' deve ser maior que zero"
    ):
        reading_plan_service.group_news_for_available_time(0)
