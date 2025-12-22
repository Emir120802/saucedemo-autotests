def test_add_item_to_cart(login_page, inventory_page):
    # Логин
    login_page.navigate()
    login_page.login("standard_user", "secret_sauce")
    
    # Добавляем товар
    inventory_page.add_backpack_to_cart()
    
    # Проверка — появилась ли "1" на иконке корзины
    assert inventory_page.get_cart_count() == "1"