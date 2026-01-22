import sqlite3
from datetime import datetime

class Purchase:
    def __init__(self, id: int, product_id: int, amount: int, currency: str, price_per_unit: float, purchase_datetime: datetime):
        self.id = id
        self.product_id = product_id
        self.amount = amount
        self.currency = currency
        self.ppu = price_per_unit
        self.datetime = purchase_datetime


    def get_product(self):
        from product import Product
        with sqlite3.connect("shop.db") as db_conn:
            cursor = db_conn.cursor()
            row = cursor.execute("SELECT id, title, advice_price, category, available FROM products WHERE id = ?", [self.product_id]).fetchone()

        return Product(id=row[0], title=row[1].strip(), advice_price=row[2], category=row[3], available=bool(row[4]))
    
    def cheaper_than(self, other) -> bool:
        if self.ppu < other.ppu:
            return True

    def more_expensive_than(self, other) -> bool:
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