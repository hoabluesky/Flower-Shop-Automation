from pages.login_page import LoginPage

# Test case for logging in a user
def test_login_user(page, app_url, username_password):

    login_page = LoginPage(page)

    login_page.navigate(app_url + "/login")

    login_page.login(username_password["username"], username_password["password"])

    assert login_page.login_successful()

# Test case for logging in with invalid password
def test_login_invalid_password(page, app_url, username_password):
    
    login_page = LoginPage(page)

    login_page.navigate(app_url + "/login")

    login_page.login(username_password["username"], "invalid_password")

    assert login_page.login_failed()

# Test case for logging in with invalid credentials
def test_login_invalid_user(page, app_url):
    
    login_page = LoginPage(page)

    login_page.navigate(app_url + "/login")

    login_page.login("invalid_user", "invalid_password")

    assert login_page.login_failed()
