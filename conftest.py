import os
import allure
import allure_commons
import pytest
from selene import browser, support
from selenium import webdriver


@pytest.hookimpl(tryfirst=True)
def pytest_configure(config):
    cwd_report = os.path.join(os.path.dirname(os.path.abspath(__file__)), "allure-results")
    allure_dir = getattr(config.option, "allure_report_dir", None)
    if not allure_dir:
        setattr(config.option, "allure_report_dir", cwd_report)


@pytest.fixture(autouse=True)
def browser_management(request):
    options = webdriver.ChromeOptions()
    options.add_argument("--window-size=1920,1080")
    options.add_argument("--incognito")
    # options.add_argument('--headless=new')
    options.add_argument("--lang=en")
    if os.environ.get("CI_RUN"):
        options.add_argument("--headless=new")
        options.add_argument("--no-sandbox")
        options.add_argument("--disable-dev-shm-usage")
    browser.config.driver_options = options

    browser.config.timeout = 5
    # browser.config.log_outer_html_on_failure = True !!! DISABLES STEPS !!!
    browser.config.reports_folder = os.path.join(os.path.dirname(os.path.abspath(__file__)), "driver-report")

    browser.config._wait_decorator = support._logging.wait_with(
        context=allure_commons._allure.StepContext
    )
    failed_before = request.session.testsfailed

    yield

    if request.session.testsfailed != failed_before:
        allure.attach(
            browser.driver.get_screenshot_as_png(),
            name="screenshot",
            attachment_type=allure.attachment_type.PNG
        )
    browser.quit()