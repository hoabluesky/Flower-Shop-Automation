class BasePage:
    def __init__(self, page):
        self.page = page
    
    def navigate(self, url):
        self.page.goto(url, wait_until="networkidle", timeout=60000)

    def click(self, locator):
        locator.click()
    
    def fill(self, locator, text):
        locator.fill(text)
    
    def get_text(self, locator):
        return locator.text_content()
    
    def get_value(self, locator):
        return locator.input_value()
    
    def is_visible(self, locator):
        return locator.is_visible()
    
    
