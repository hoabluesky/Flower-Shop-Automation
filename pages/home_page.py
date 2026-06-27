from pages.base_page import BasePage

class HomePage(BasePage):
  
    def search_input(self):
        return self.page.get_by_role("textbox", name="Search flowers")
    
    def search_button(self):
        return self.page.get_by_role("button", name="Search")
    
    def flower_heading(self, flower_name):
        return self.page.get_by_role("heading", name=flower_name)

    def add_to_cart_button(self):
        return self.page.get_by_role("link", name="Add to Cart")

    def search_flower(self, flower_name):
        self.fill(self.search_input(), flower_name)
        self.click(self.search_button())
        
    def flower_is_visible(self, flower_name):
        return self.is_visible(self.flower_heading(flower_name))
    
    def add_flower_to_cart(self):
        add_to_cart_button = self.add_to_cart_button()
        self.click(add_to_cart_button)
     
    

    