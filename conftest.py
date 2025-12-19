# conftest.py (Обновленная версия)
import pytest
from playwright.sync_api import sync_playwright
from pages.login_page import LoginPage

# Добавляем опцию запуска через консоль
def pytest_addoption(parser):
    parser.addoption("--headless", action="store_true", default=False, help="Run browser in headless mode")

@pytest.fixture(scope="function")
def page_fixture(pytestconfig):
    headless_mode = pytestconfig.getoption("--headless") # Читаем настройку
    
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=headless_mode)
        context = browser.new_context()
        page = context.new_page()
        yield page
        browser.close()

@pytest.fixture(scope="function")
def login_page(page_fixture):
    return LoginPage(page_fixture)