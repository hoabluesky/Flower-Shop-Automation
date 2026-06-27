from pages.base_page import BasePage

class RegisterPage(BasePage):

    def username_input(self):
        return self.page.locator("input[name=\"username\"]")
    
    def password_input(self):
        return self.page.locator("input[name=\"password\"]")
    
    def register_button(self):
        return self.page.get_by_role("button", name="Register")

    def register(self, username, password):
        self.click(self.username_input())
        self.fill(self.username_input(), username)
        self.click(self.password_input())
        self.fill(self.password_input(), password)
        self.click(self.register_button())

    def registration_successful(self):
        return self.page.get_by_text("Registration successful").is_visible()
    
    def registration_failed_due_to_duplicate(self):
        return self.page.get_by_text("Username already exists").is_visible()
    
    def registration_failed_due_to_blank_fields(self):
        return self.page.get_by_text("Username and password cannot be blank").is_visible()
    

    
        





    
 






