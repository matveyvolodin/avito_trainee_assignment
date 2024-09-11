
from selene import be, have, browser, query
from selene.support.shared.jquery_style import s, ss

# Urls
main_page_url = "https://makarovartem.github.io/frontend-avito-tech-test-assignment"

# Locators
by_category_dropdown = s('(//span[@class="ant-select-selection-item"])[2]')
genre_elements = ss('//div[contains(@class, "ant-typography css-17a39f8") and text()="Genre: "]')
paginator_next_page_button = s('(//button[@class="ant-pagination-item-link"])[2]')
paginator_number_button = s('(//li[@title=2])[1]')

game_card_container = s('(//div[@class="ant-card-body"])[1]')
back_to_main_button = s('//button[@type="button"]')
page_game_titles = ss('//div[@class="_container_vlg32_23"]/div[1]/h1')


def visit(url):
    browser.open(url)


def select_dropdown_by_genre_option(option):
    s(f'//div[contains(@class, "ant-select-item") and text()="{option}"]').click()


def create_game_titles_set():
    page_game_titles.should(have.size_greater_than(0))
    game_titles_set = {title.get(query.text) for title in page_game_titles}
    return game_titles_set

