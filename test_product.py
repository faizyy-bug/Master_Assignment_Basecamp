import pytest
from product import Product

def test_product():
    prod = Product(1, """
                LISEN USB C to Lightning Cable, 240W 4 in 1 Charging Cable 6.6FT,
                Chubby USB A/C to C/Lightning with Light for iPhone 16e 15 14 Pro/MacBook Air 17/iPad/Samsung/Switch 2, 
                Multi Chargers for All Devices""", 15.99, "Laptops", True)
    
    assert prod.get_ratings() == [5, 74, 4, 8, 5]
    assert prod.get_purchases() == [1, 3, 2, 2, 1, 1, 1, 2, 2]

    return True

print(test_product())
