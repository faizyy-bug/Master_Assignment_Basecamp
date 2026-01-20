import sqlite3
from product import Product

class Purchase:
    def init(self, id: int, product: int, amount: int, currency: str, price_per_unit: float):
        self.id = id
        self.product = product
        self.amount = amount
        self.currency = currency
        self.ppu = price_per_unit
        self.db_conn = sqlite3.connect("shop.db")
        self.db_conn.execute("""INSERT INTO purchases
                             (id, product, amount, currency, price_per_unit) VALUES(?, ?, ?, ?, ?)""",
                             [self.id, self.product, self.amount, self.currency, self.ppu])
        self.db_conn.commit()
        
    def get_product() -> Product:



      # Representation method
    # This will format the output in the correct order
    # Format is @dataclass-style: Classname(attr=value, attr2=value2, ...)
    def __repr__(self) -> str:
        sorted_items = sorted(self.__dict__.items(), key=lambda item: item[0])
        return "{}({})".format(
            type(self).__name__,
            ", ".join([f"{key}={value!s}" for key, value in sorted_items]),
        )