import pytest
import allure
from playwright.sync_api import sync_playwright

@allure.feature("Mobile Testing")
@allure.story("Login on iPhone 14")
def test_login_mobile():
    with sync_playwright() as p:
        # Эмулируем iPhone 14
        iphone = p.devices['iPhone 14']
        browser = p.chromium.launch(headless=True)
        # Создаем контекст с параметрами телефона (размер экрана, user-agent)
        context = browser.new_context(**iphone)
        page = context.new_page()

        with allure.step("Navigate to Saucedemo on mobile"):
            page.goto("https://www.saucedemo.com/")
        
        with allure.step("Perform login"):
            page.fill("#user-name", "standard_user")
            page.fill("#password", "secret_sauce")
            page.click("#login-button")

        with allure.step("Verify successful login on mobile"):
            assert page.url == "https://www.saucedemo.com/inventory.html"
            # Проверяем, что заголовок виден на маленьком экране
            assert page.is_visible(".app_logo")

        browser.close()