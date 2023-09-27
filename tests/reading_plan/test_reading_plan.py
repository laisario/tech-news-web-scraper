from tech_news.analyzer.reading_plan import (
    ReadingPlanService,
)  # noqa: F401, E261, E501
from tech_news.database import db
import pytest
from tests.assets.news import NEWS

NEW_NOTICE_0 = NEWS[0]
NEW_NOTICE_1 = NEWS[1]
NEW_NOTICE_2 = NEWS[2]
NEW_NOTICE_13 = NEWS[13]


def test_reading_plan_group_news():
    reading_plan_service = ReadingPlanService()
    db.news.delete_many({})
    db.news.insert_one(NEW_NOTICE_0)
    db.news.insert_one(NEW_NOTICE_1)
    db.news.insert_one(NEW_NOTICE_2)
    db.news.insert_one(NEW_NOTICE_13)
    expected = (
        {
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
            "unreadable": [
                ("noticia_13", 15)
            ]
        }
    )
    assert reading_plan_service.group_news_for_available_time(10) == expected
    with pytest.raises(
        ValueError, match="Valor 'available_time' deve ser maior que zero"
    ):
        reading_plan_service.group_news_for_available_time(0)
