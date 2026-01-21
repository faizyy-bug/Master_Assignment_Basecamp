import pytest
from rating import Rating
from product import Product

def test_rating():
    rate = Rating(1, 1, 5, 1, 7)
    prod = rate.get_product()
    
    assert prod.id == 1
    # assert prod.title.strip() == "LISEN USB C to Lightning Cable, 240W 4 in 1 Charging Cable 6.6FT,Chubby USB A/C to C/Lightning with Light for iPhone 16e 15 14 Pro/MacBook Air 17/iPad/Samsung/Switch 2, Multi Chargers for All Devices"
    
    assert prod.advice_price == 15.99
    assert prod.category == "Laptops"
    assert prod.available == True

    result = float(5 - 1) / (7 - 1)
    assert rate.get_normalized_rating() == float(5 - 1) / (7 - 1)
    assert rate.get_rating_in_scale(1, 8) == result * (8 - 1) + (1) 
    assert rate.is_rating_higher_than(3) == True

    return True

print(test_rating())




if __name__  == "__main__":
    test_rating()