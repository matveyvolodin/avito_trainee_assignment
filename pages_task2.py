from selene import be, have, browser, query
from selene.support.shared.jquery_style import s, ss

# Urls
main_page_url = "https://makarovartem.github.io/frontend-avito-tech-test-assignment"

# Locators
by_category_dropdown = s('(//span[@class="ant-select-selection-item"])[2]')
genre_elements = ss('//div[contains(@class, "ant-typography css-17a39f8") and text()="Genre: "]')
paginator_number2_button = s('(//li[@title=2])[1]')
paginator_number3_button = s('(//li[@title=3])[1]')
paginator_next_page_button = s('(//li[@title="Next Page"])[1]')
paginator_previous_page_button = s('(//li[@title="Previous Page"])[1]')

game_card_container = s('(//div[@class="ant-card-body"])[1]')
back_to_main_button = s('//button[@type="button"]')
page_game_titles = ss('//div[@class="_container_vlg32_23"]/div[1]/h1')


def visit(url):
    browser.open(url)


def select_dropdown_by_genre_option(option):
    s(f'//div[contains(@class, "ant-select-item") and text()="{option}"]').click()


def check_genre(expected_actual_text):
    while True:
        genre_elements.should(have.size_greater_than(0))
        for element in genre_elements:
            element.should(have.text(expected_actual_text))
        if paginator_next_page_button.should(be.clickable):
            paginator_next_page_button.click()
        else:
            break


def create_game_titles_set():
    page_game_titles.should(have.size_greater_than(0))
    game_titles_set = {title.get(query.text) for title in page_game_titles}
    return game_titles_set


def create_actual_unsorted_genre_set():
    actual_genre_set = set()
    while True:
        genre_elements.should(have.size_greater_than(0))
        for element in genre_elements:
            actual_genre_set.add(element.get(query.text))
        if paginator_next_page_button.should(be.clickable):
            paginator_next_page_button.click()
        else:
            break
    return actual_genre_set
