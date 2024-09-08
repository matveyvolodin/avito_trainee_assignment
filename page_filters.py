
from selene import be, have, browser
from selene.support.shared.jquery_style import s, ss

# Urls
main_page_url = "https://makarovartem.github.io/frontend-avito-tech-test-assignment"

# Locators
by_category_dropdown = s('(//span[@class="ant-select-selection-item"])[2]')
genre_elements = ss('//div[contains(@class, "ant-typography css-17a39f8") and text()="Genre: "]')
paginator_next_page_button = s('(//button[@class="ant-pagination-item-link"])[2]')


def visit_page(url):
    browser.open(url)


def select_dropdown_by_genre_option(option):
    s(f'//div[contains(@class, "ant-select-item") and text()="{option}"]').click()