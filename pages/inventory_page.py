from pages.base_page import BasePage

class InventoryPage(BasePage):
    # Локаторы
    CART_BADGE = ".shopping_cart_badge"
    CART_LINK = ".shopping_cart_link"

    def get_cart_count(self):
        """
        Возвращает количество товаров в корзине. 
        Если товаров нет — возвращает "0", чтобы тест не падал по таймауту.
        """
        try:
            # Ждем появления бейджа короткое время (например, 2 секунды)
            self.page.wait_for_selector(self.CART_BADGE, state="visible", timeout=2000)
            return self.page.inner_text(self.CART_BADGE)
        except:
            # Если бейдж не появился (корзина пуста), возвращаем 0 
            return "0"

    def go_to_cart(self):
        self.page.click(self.CART_LINK)

    def add_item_to_cart_by_name(self, item_name):
        """
        Динамически формирует ID кнопки на основе названия товара.
        Учитывает особенности написания (нижний регистр и тире вместо пробелов).
        """
        # Sauce Labs Bolt T-Shirt -> sauce-labs-bolt-t-shirt
        clean_name = item_name.lower().replace(" ", "-")
        selector = f"button[id='add-to-cart-{clean_name}']"
        
        # Ждем, пока кнопка станет доступной, и кликаем
        self.page.wait_for_selector(selector, state="visible", timeout=5000)
        self.page.click(selector)