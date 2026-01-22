import pytest
from purchase import Purchase

def test_purchase():

    pur = Purchase(1, 1, 1, "VND", 379107.69, "2023-10-01 10:00:00")
    cheaper_then = Purchase(1, 1, 3, "VND", 19.99, "2023-10-01 10:00:00")

    pur.cheaper_than(cheaper_then) == False
    pur.more_expensive_than(cheaper_then) == True

    return True

print(test_purchase())
