import pytest
from currency_exchange import CurrencyExchange

def test_currency():
    cur = CurrencyExchange()

    assert cur.convert(1.00, "USD", "EUR") == 1.0 *  (1.08/1.0)

    return True


print(test_currency())

if __name__ == "__main__":
    test_currency()

