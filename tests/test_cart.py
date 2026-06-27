from pages.cart_page import CartPage

# Test case for verifying flowers in the cart
def test_cart_functionality(page, app_url, flower_in_cart):

    cart_page = CartPage(page)

    cart_page.navigate(app_url + "/cart")

    assert cart_page.flower_is_in_cart(flower_in_cart[0]), "Flower not found in cart."

    assert cart_page.flower_is_in_cart(flower_in_cart[1]), "Flower not found in cart."

# Test case for chaging the quantity of a flower in the cart
def test_cart_change_quantity(page, app_url, flower_in_cart):

    cart_page = CartPage(page)

    cart_page.navigate(app_url + "/cart")

    cart_page.change_quantity(flower_in_cart[0], 3)

    assert cart_page.get_quantity(flower_in_cart[0]) == 3, "Quantity not updated correctly."
