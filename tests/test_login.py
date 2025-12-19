# tests/test_login.py
import pytest

def test_valid_login(login_page):
    """Тест успешного входа в систему"""
    login_page.navigate()
    login_page.login("standard_user", "secret_sauce")
    
    # Проверка (Assert): проверяем, что урл изменился на инвентарь
    assert "inventory.html" in login_page.page.url

def test_locked_out_user(login_page):
    """Тест заблокированного пользователя (Негативный кейс)"""
    login_page.navigate()
    login_page.login("locked_out_user", "secret_sauce")
    
    # Проверка текста ошибки
    error = login_page.get_error_message()
    assert "Sorry, this user has been locked out" in error