from playwright.sync_api import Page

class BasePage:
    def __init__(self, page: Page):
        self.page = page

    def open(self, url):
        self.page.goto(url)

    def find(self, selector):
        return self.page.locator(selector)
    
    def get_title(self):
        return self.page.title()