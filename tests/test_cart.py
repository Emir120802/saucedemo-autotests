def test_add_item_to_cart(login_page, inventory_page):
    # Шаг 1: Логин
    login_page.navigate()
    login_page.login("standard_user", "secret_sauce")
    
    # Шаг 2: Добавляем товар
    inventory_page.add_backpack_to_cart()
    
    # Шаг 3: Проверка — появилась ли "1" на иконке корзины
    assert inventory_page.get_cart_count() == "1000"