from pages.register_page import RegisterPage
from datetime import datetime

username = f"user_{datetime.now().strftime('%Y%m%d%H%M%S')}"
password = "TestPassword123!"

username_duplicate=username  # Using the same username to test duplicate registration
password_for_duplicate="AnotherPassword123!"  # Different password for duplicate registration

# Test case for registering a new user
def test_register_user(page, app_url):

    register_page = RegisterPage(page)

    register_page.navigate(app_url + "/register")

    register_page.register(username, password)

    assert register_page.registration_successful()


# Test case for registering a duplicate user
def test_register_duplicate_user(page, app_url):
    
    register_page = RegisterPage(page)

    register_page.navigate(app_url + "/register")

    register_page.register(username_duplicate, password_for_duplicate)

    assert register_page.registration_failed_due_to_duplicate()
    
# Test case for registering with blank username and password
def test_register_blank_username_password(page, app_url):
   
    register_page = RegisterPage(page)

    register_page.navigate(app_url + "/register")

    register_page.register("", "")

    assert register_page.registration_failed_due_to_blank_fields()





                       



