import pytest
import allure
from playwright.sync_api import sync_playwright
from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage

def pytest_addoption(parser):
    parser.addoption("--headless", action="store", default=True, help="Run browser in headless mode")

@pytest.fixture(scope="function")
def page_fixture(pytestconfig):
    headless_mode = pytestconfig.getoption("--headless")
    if isinstance(headless_mode, str):
        headless_mode = headless_mode.lower() == "true"
    
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=headless_mode)
        context = browser.new_context()
        page = context.new_page()
        yield page
        browser.close()

@pytest.fixture(scope="function")
def login_page(page_fixture):
    return LoginPage(page_fixture)

@pytest.fixture(scope="function")
def inventory_page(page_fixture):
    return InventoryPage(page_fixture)

# Хук для снятия скриншота при падении теста
@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    rep = outcome.get_result()
    
    # Проверяем, что это этап выполнения теста ('call') и он завершился неудачей
    if rep.when == 'call' and rep.failed:
        page = item.funcargs.get('page_fixture')
        if page:
            # Делаем скриншот и прикрепляем его к отчету Allure
            screenshot = page.screenshot(full_page=True)
            allure.attach(
                screenshot,
                name=f"failure_{item.name}",
                attachment_type=allure.attachment_type.PNG
            )

           