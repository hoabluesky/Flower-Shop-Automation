from pages.base_page import BasePage

class LoginPage(BasePage):

    def username_input(self):
        return self.page.locator("input[name=\"username\"]")
    
    def password_input(self):
        return self.page.locator("input[name=\"password\"]")
    
    def login_button(self):
        return self.page.get_by_role("button", name="Login")

    def login(self, username, password):
        self.click(self.username_input())
        self.fill(self.username_input(), username)
        self.click(self.password_input())
        self.fill(self.password_input(), password)
        self.click(self.login_button())

    def login_successful(self):
        return self.page.get_by_text("Login successful").is_visible()
    
    def login_failed(self):
        return self.page.get_by_text("Invalid credentials").is_visible()
    