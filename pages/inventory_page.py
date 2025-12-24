from pages.base_page import BasePage

class InventoryPage(BasePage):
    # Локаторы
    ADD_TO_CART_SAUCE_BACKPACK = "#add-to-cart-sauce-labs-backpack"
    CART_BADGE = ".shopping_cart_badge"
    CART_LINK = ".shopping_cart_link"

    def add_backpack_to_cart(self):
        self.page.click(self.ADD_TO_CART_SAUCE_BACKPACK)

    def get_cart_count(self):
        # Добавляем ожидание появления элемента перед тем как брать текст
        self.page.wait_for_selector(self.CART_BADGE, timeout=5000)
        return self.page.inner_text(self.CART_BADGE)

    def go_to_cart(self):
        self.page.click(self.CART_LINK)

    def add_item_to_cart_by_name(self, item_name):
        # Очищаем имя от лишних знаков и заменяем пробелы на тире
        selector_name = item_name.lower().replace(" ", "-")
        selector = f"[id^='add-to-cart-{selector_name}']" # Используем поиск по началу ID
        self.page.click(selector)