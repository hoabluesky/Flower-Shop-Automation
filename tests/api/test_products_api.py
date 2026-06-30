git statusfrom api.api_client import APIClient
MAX_RESPONSE_TIME = 2  # seconds

def test_get_products():
    client = APIClient("https://flower-shop-app.onrender.com/api")
    response = client.get("products")
    
    assert response.status_code == 200
    
    data=response.json()
    
    assert isinstance(data, list)  # Assuming the response is a list of products
    assert len(data) > 0  # Assuming there is at least one product

    for product in data:
        assert isinstance(product, dict)  # Each product should be a dictionary
        assert isinstance(product["id"], int)  # Assuming 'id' is an integer
        assert isinstance(product["name"], str)  # Assuming 'name' is a string
        assert isinstance(product["price"], (int, float))  # Assuming 'price' is a number
        assert isinstance(product["description"], str)  # Assuming 'description' is a string
    
    required_keys = ["id", "name", "price", "description"]
    for product in data:
        for key in required_keys:
            assert key in product

    assert response.elapsed.total_seconds() < MAX_RESPONSE_TIME, f"Response time exceeded {MAX_RESPONSE_TIME} seconds"

