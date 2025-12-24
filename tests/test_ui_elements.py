import allure
import pytest

@allure.feature("UI Elements")
@allure.story("Sorting functionality")
def test_sorting_az(login_page, inventory_page):
    with allure.step("Login to application"):
        login_page.navigate()
        login_page.login("standard_user", "secret_sauce")
    
    with allure.step("Verify default sorting is A-Z"):
        # Проверяем, что первый товар — это Backpack
        first_item = inventory_page.page.locator(".inventory_item_name").first
        assert first_item.inner_text() == "Wrong Item"

@allure.feature("UI Elements")
@allure.story("Logout functionality")
def test_logout(login_page, inventory_page):
    with allure.step("Login to application"):
        login_page.navigate()
        login_page.login("standard_user", "secret_sauce")
    
    with allure.step("Open burger menu and logout"):
        inventory_page.page.click("#react-burger-menu-btn")
        inventory_page.page.click("#logout_sidebar_link")
    
    with allure.step("Verify redirection to login page"):
        assert login_page.page.url == "https://www.saucedemo.com/"