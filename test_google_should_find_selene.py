import pytest
from selene.support.shared import browser
from selene import be, have

@pytest.fixture
def browser_size():
    browser.config.window_width = 1366
    browser.config.window_height = 768
@pytest.fixture
def open_browser():
    browser.open('https://google.com')

def test_search_1(browser_size, open_browser):
     browser.element('[name="q"]').should(be.blank).type('yashaka/selene').press_enter()
     browser.element('[id="search"]').should(have.text('Selene - User-oriented Web UI browser tests in Python'))


def test_search_1(browser_size, open_browser):
    browser.element('[name="q"]').should(be.blank).type('шщдбьрпенорлодшзжлюбооецукер1234567пнкпапримимопмсчапм').press_enter()
    browser.element('[id="result-stats"]').should(have.text('Результатов: примерно 0'))