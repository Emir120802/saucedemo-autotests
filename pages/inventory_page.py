from pages.base_page import BasePage

class InventoryPage(BasePage):
    # Локаторы
    CART_BADGE = ".shopping_cart_badge"
    CART_LINK = ".shopping_cart_link"
    # Добавляем локатор для рюкзака обратно
    ADD_TO_CART_SAUCE_BACKPACK = "#add-to-cart-sauce-labs-backpack"

    def add_backpack_to_cart(self):
        """Метод для обратной совместимости со старыми тестами"""
        self.page.wait_for_selector(self.ADD_TO_CART_SAUCE_BACKPACK, state="visible")
        self.page.click(self.ADD_TO_CART_SAUCE_BACKPACK)

    def get_cart_count(self):
        """Возвращает количество товаров или '0', если корзина пуста"""
        try:
            self.page.wait_for_selector(self.CART_BADGE, state="visible", timeout=2000)
            return self.page.inner_text(self.CART_BADGE)
        except:
            return "0"

    def go_to_cart(self):
        self.page.click(self.CART_LINK)

    def add_item_to_cart_by_name(self, item_name):
        """Универсальный метод для добавления любого товара по имени"""
        clean_name = item_name.lower().replace(" ", "-")
        selector = f"button[id='add-to-cart-{clean_name}']"
        
        self.page.wait_for_selector(selector, state="visible", timeout=5000)
        self.page.click(selector)