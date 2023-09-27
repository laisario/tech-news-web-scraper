from tech_news.analyzer.reading_plan import (
    ReadingPlanService,
)  # noqa: F401, E261, E501
import pytest
from tests.assets.news import NEWS
from unittest.mock import patch


NEW_NOTICE_0 = NEWS[0]
NEW_NOTICE_1 = NEWS[1]
NEW_NOTICE_2 = NEWS[2]
NEW_NOTICE_13 = NEWS[13]


def test_reading_plan_group_news():
    reading_plan_service = ReadingPlanService()

    mock_db = [NEW_NOTICE_0, NEW_NOTICE_1, NEW_NOTICE_2, NEW_NOTICE_13]

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
        find_news_mock.return_value = mock_db
        result = reading_plan_service.group_news_for_available_time(10)
    assert result == expected

    with pytest.raises(
        ValueError, match="Valor 'available_time' deve ser maior que zero"
    ):
        reading_plan_service.group_news_for_available_time(0)
