
from selene import be, have, browser
from selene.support.shared.jquery_style import s, ss

# Urls
main_page_url = "https://makarovartem.github.io/frontend-avito-tech-test-assignment"

# Locators
by_category_dropdown = s('(//span[@class="ant-select-selection-item"])[2]')
genre_elements = ss('//div[contains(@class, "ant-typography css-17a39f8") and text()="Genre: "]')
paginator_next_page_button = s('(//button[@class="ant-pagination-item-link"])[2]')

game_card_container = s('(//div[@class="ant-card-body"])[1]')
back_to_main_button = s('//button[@type="button"]')


def visit(url):
    browser.open(url)


def select_dropdown_by_genre_option(option):
    s(f'//div[contains(@class, "ant-select-item") and text()="{option}"]').click()