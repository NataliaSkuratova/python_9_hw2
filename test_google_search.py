from selene.support.shared import browser
from selene import be, have
import pytest

@pytest.fixture
def browser_configs():
    browser.config.window_width = 1920
    browser.config.window_height = 1080
    yield
    browser.quit()

def test_google_search_should_find(browser_configs):
    browser.open('https://google.com')
    browser.element('[name="q"]').should(be.blank).type('selene').press_enter()
    browser.element('[id="search"]').should(have.text('Selene - User-oriented Web UI browser tests in Python'))

def test_google_search_should_not_find(browser_configs):
    browser.open('https://www.google.ru')
    browser.element('[name="q"]').should(be.blank).type('safdgfdgfdgf').press_enter()
    browser.element('[class="card-section"]').should(have.text('Your search - safdgfdgfdgf - did not match any documents.'))
