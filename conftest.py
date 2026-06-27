import pytest


# Fixture to open the homepage of the application
@pytest.fixture
def app_url():
    return "https://flower-shop-app.onrender.com"



# Fixture to register a user and return the username and password for login tests
@pytest.fixture
def username_password(page, app_url):
    from pages.register_page import RegisterPage
    from datetime import datetime

    username = f"user_{datetime.now().strftime('%Y%m%d%H%M%S')}"
    password = "TestPassword123!"

    register_page = RegisterPage(page)
    register_page.navigate(app_url + "/register")
    register_page.register(username, password)
 
    username_password= {
        "username": username, 
        "password": password
    }
    
    assert register_page.registration_successful(), "Registration failed, cannot proceed with login tests."
    return username_password


# Fixture to add a flower to the cart and return the flower name for cart tests
@pytest.fixture
def flower_in_cart(page, app_url):

    from pages.home_page import HomePage
    from test_data.flowers import FLOWERS

    home_page = HomePage(page)
    home_page.navigate(app_url)

    flower_list=[]
    # Add the first flower from the FLOWERS list to the cart
    flower_name = FLOWERS[0]
    home_page.search_flower(flower_name)
    home_page.add_flower_to_cart()
    flower_list.append(flower_name)

    # Get the last flower from the FLOWERS list to the cart
    flower_name = FLOWERS[-1]  
    home_page.search_flower(flower_name)
    home_page.add_flower_to_cart()
    flower_list.append(flower_name)

    assert home_page.flower_is_visible(flower_name), "Flower not added to cart successfully."
    return flower_list 


