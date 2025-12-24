from pages.base_page import BasePage

class InventoryPage(BasePage):
    # Локаторы
    CART_BADGE = ".shopping_cart_badge"
    CART_LINK = ".shopping_cart_link"
    ADD_TO_CART_SAUCE_BACKPACK = "#add-to-cart-sauce-labs-backpack"

    def add_backpack_to_cart(self):
        """Метод для обратной совместимости: добавляет рюкзак в корзину"""
        self.page.wait_for_selector(self.ADD_TO_CART_SAUCE_BACKPACK, state="visible", timeout=5000)
        self.page.click(self.ADD_TO_CART_SAUCE_BACKPACK)

    def get_cart_count(self):
        """Возвращает число товаров в корзине или '0', если счетчика нет"""
        try:
            self.page.wait_for_selector(self.CART_BADGE, state="visible", timeout=2000)
            return self.page.inner_text(self.CART_BADGE)
        except:
            return "0"

    def go_to_cart(self):
        self.page.click(self.CART_LINK)

    def add_item_to_cart_by_name(self, item_name):
        """Универсальный метод добавления товара по его названию"""
        clean_name = item_name.lower().replace(" ", "-")
        selector = f"button[id='add-to-cart-{clean_name}']"
        
        self.page.wait_for_selector(selector, state="visible", timeout=5000)
        self.page.click(selector)