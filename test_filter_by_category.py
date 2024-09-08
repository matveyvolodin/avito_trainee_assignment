import allure
import pytest
from page_filters import *


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
@allure.title('TC_001_01 | Filters > Filtering by category: mmorpg')
def test_filtering_by_category(genre, expected_actual_text):
    visit_page(main_page_url)
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

