import allure
import pytest
from pages_task2 import *
from selene import be, have, browser


@pytest.mark.parametrize('genre, expected_actual_text',
                         [
                             ("mmorpg", "MMORPG"),
                             ("shooter", "Shooter"),
                             ("strategy", "Strategy"),
                             ("moba", "MOBA"),
                             ("racing", "Racing"),
                             ("sports", "Sports"),
                             ("social", "Social")
                         ]
                         )
@allure.title('TC_001_01 | Filters > Filtering by category')
def test_filtering_by_category(genre, expected_actual_text):
    visit(main_page_url)
    by_category_dropdown.click()
    select_dropdown_by_genre_option(genre)
    # Цикл проверки жанра карточек в выдаче после фильтрации по category на всех страницах пагинатора
    check_genre(expected_actual_text)


@allure.title('TC_001_08 | Filters > Attempt to filter by category: ("not chosen"')
def test_filtering_by_category_no_chosen():
    visit(main_page_url)
    by_category_dropdown.click()
    select_dropdown_by_genre_option("mmorpg")
    by_category_dropdown.click()
    select_dropdown_by_genre_option("not chosen")
    full_genre_set = {"MMORPG", "Shooter", "Strategy", "MOBA", "Racing", "Sports", "Social"}
    actual_genre_set = create_actual_unsorted_genre_set()
    assert full_genre_set.issubset(actual_genre_set)


@allure.title('TC_002_01 | Redirecting > Redirecting to the main page using the "Back to main" button')
def test_redirecting_to_the_main_page_using_back_to_main_button():
    visit(main_page_url)
    game_card_container.should(be.clickable).click()
    back_to_main_button.should(be.clickable).click()
    # Проверка фактического Url
    browser.should(have.url(main_page_url))


@allure.title('TC_003_01 | Paginator > Navigating using the paginator number button')
def test_navigating_using_the_paginator_number_button():
    visit(main_page_url)
    # Созданием множества с названиями игр с первой страницы пагинатора в переменной titles_set_page1
    titles_set_page1 = create_game_titles_set()
    paginator_number2_button.should(be.clickable).click()
    # Проверка 2 кнопки пагинатора на "активность"
    paginator_number2_button.should(have.css_class('ant-pagination-item-active'))
    # Созданием множества с названиями игр со второй страницы пагинатора в переменной titles_set_page2
    titles_set_page2 = create_game_titles_set()
    # Проверка пересечения множеств (игры, отображенные на страницах не повторяются)
    assert not titles_set_page1.intersection(titles_set_page2)


@allure.title('TC_003_02 | Paginator > Navigating using the paginator "Next Page" button')
def test_navigating_using_the_paginator_next_page_button():
    visit(main_page_url)
    titles_set_page1 = create_game_titles_set()
    paginator_next_page_button.should(be.clickable).click()
    paginator_number2_button.should(have.css_class('ant-pagination-item-active'))
    titles_set_page2 = create_game_titles_set()
    assert not titles_set_page1.intersection(titles_set_page2)


@allure.title('TC_003_03 | Paginator > Navigating using the paginator "Previous Page" button')
def test_navigating_using_the_paginator_previous_page_button():
    visit(main_page_url)
    paginator_number3_button.should(be.clickable).click()
    titles_set_page3 = create_game_titles_set()
    paginator_previous_page_button.should(be.clickable).click()
    paginator_number2_button.should(have.css_class('ant-pagination-item-active'))
    titles_set_page2 = create_game_titles_set()
    assert not titles_set_page3.intersection(titles_set_page2)

