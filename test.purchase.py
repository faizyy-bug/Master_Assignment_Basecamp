import pytest
from purchase import Purchase

def test_purchase():

    pur = Purchase(1, 1, 1, "VND", 379107.69)

    pur.cheaper_than(18.99) == False
    pur.more_expensive_than(18.99) == True

    return True


print(test_purchase()) 

if __name__ == "__main__":
    test_purchase()

    