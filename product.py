import sqlite3
import json
from rating import Rating


class Product:

    def __init__(self, id: int, title: str, advice_price: float, category: str, available: bool):
        self.id = id
        self.title = title
        self.advice_price = advice_price
        self.category = category
        self.available = available
        self.db_conn = sqlite3.connect("shop.db")
      

    def get_ratings(self) -> list[Rating]:
        rows = self.db_conn.execute("SELECT rating FROM ratings WHERE product_id = ? ", self.id)
        ratings = rows.fetchall()

        return list(ratings)        
    
    def get_purchase(self, id, title, advice, category, available) -> list:
        pass

      # Representation method
    # This will format the output in the correct order
    # Format is @dataclass-style: Classname(attr=value, attr2=value2, ...)
    def __repr__(self) -> str:
        sorted_items = sorted(self.__dict__.items(), key=lambda item: item[0])
        return "{}({})".format(
            type(self).__name__,
            ", ".join([f"{key}={value!s}" for key, value in sorted_items]),
        )

    
    