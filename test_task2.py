import allure
import pytest
from selene import browser
from pages_task2 import *
from time import sleep


@pytest.mark.parametrize('genre, expected_actual_text',
                         [
                             ("mmorpg", "MMORPG"),
                             ("shooter", "Shooter"),
                             ("strategy", "Strategy"),
                             ("moba", "MOBA"),
                             ("racing", "RACING"),
                             ("sports", "Sports"),
                             ("social", "Social")
                         ]
                         )
@allure.title('TC_001_01 | Filters > Filtering by category')
def test_filtering_by_category(genre, expected_actual_text):
    visit(main_page_url)
    by_category_dropdown.click()
    select_dropdown_by_genre_option(genre)
    while True:
        genre_elements.should(have.size_greater_than(0))
        for element in genre_elements:
            element.should(have.text(expected_actual_text))
        if paginator_next_page_button.should(be.clickable):
            paginator_next_page_button.should(be.visible).click()
        else:
            break


@allure.title('TC_002_01 | Redirecting > Redirecting to the main page using the "Back to main" button')
def test_redirecting_to_the_main_page_using_back_to_main_button():
    visit(main_page_url)
    game_card_container.should(be.clickable).click()
    back_to_main_button.should(be.clickable).click()
    browser.should(have.url(main_page_url))

