import allure

@allure.feature("Auth")  # Группировка по функционалу
@allure.story("Login with valid credentials") # Конкретный сценарий
def test_valid_login(login_page, inventory_page):
    with allure.step("Navigate to the login page"):
        login_page.navigate()
    
    with allure.step("Submit login form"):
        login_page.login("standard_user", "secret_sauce")
    
    with allure.step("Verify successful redirection"):
        assert inventory_page.get_cart_count() is not None