import pytest

from pages.home_page import HomePage
from test_data.flowers import FLOWERS
from test_data.flowers import INVALID_FLOWERS

@pytest.mark.parametrize("flower_name", FLOWERS)

def test_search_existing_flower(page, app_url, flower_name):

    home_page = HomePage(page)

    home_page.navigate(app_url)

    home_page.search_flower(flower_name)

    assert home_page.flower_is_visible(flower_name)

@pytest.mark.parametrize("flower_name", INVALID_FLOWERS)

def test_search_non_existing_flower(page, app_url, flower_name):

    home_page = HomePage(page)

    home_page.navigate(app_url)

    home_page.search_flower(flower_name)

    assert not home_page.flower_is_visible(flower_name)