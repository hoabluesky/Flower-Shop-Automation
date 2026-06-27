from pages.base_page import BasePage
class CartPage(BasePage):

    def flower_is_in_cart(self, flower_name):
        return self.page.get_by_role("cell", name=flower_name).is_visible()

    def change_quantity(self, flower_name, quantity):
        quantity_input = self.page.get_by_role("row", name=flower_name).get_by_role("spinbutton")       
        self.fill(quantity_input, str(quantity))
        update_button = self.page.get_by_role("row", name=flower_name).get_by_role("button", name="Update")
        self.click(update_button)

    def get_quantity(self, flower_name):
        quantity_input = self.page.get_by_role("row", name=flower_name).get_by_role("spinbutton")
        return int(self.get_value(quantity_input))


    