import sqlite3
from product import Product

class Purchase:
    def __init__(self, id: int, product: int, amount: int, currency: str, price_per_unit: float):
        self.id = id
        self.product = product
        self.amount = amount
        self.currency = currency
        self.ppu = price_per_unit
        self.db_conn = sqlite3.connect("shop.db")

    def get_product(self) -> Product:
        cursor = self.db_conn.cursor()
        row = cursor.execute("SELECT title, advice_price, category, available FROM products WHERE id = ?", [self.id])

        return Product(*row)
    
    def cheaper_than(self, other) -> bool:
        if self.ppu < other.ppu:
            return True

    def more_expensive_then(self, other) -> bool:
        if self.ppu > other.ppu:
            return True
          

      # Representation method
    # This will format the output in the correct order
    # Format is @dataclass-style: Classname(attr=value, attr2=value2, ...)
    def __repr__(self) -> str:
        sorted_items = sorted(self.__dict__.items(), key=lambda item: item[0])
        return "{}({})".format(
            type(self).__name__,
            ", ".join([f"{key}={value!s}" for key, value in sorted_items]),
        )