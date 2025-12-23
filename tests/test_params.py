import allure
import pytest
@pytest.mark.parametrize("item_name", [
    "Sauce Labs Backpack",
    "Sauce Labs Bike Light",
    "Sauce Labs Bolt T-Shirt"
])
def test_multiple_items_addition(login_page, inventory_page, item_name):
    login_page.navigate()
    login_page.login("standard_user", "secret_sauce")
    
    # Добавляем товар, имя которого пришло из параметров
    inventory_page.add_item_to_cart_by_name(item_name)
    
    # Проверяем, что в корзине появился 1 предмет
    assert inventory_page.get_cart_count() == "1"