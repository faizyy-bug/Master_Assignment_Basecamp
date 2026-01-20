import sqlite3
import json
# from rating import Rating
# from purchase import Purchase


class Product:

    def __init__(self, id: int, title: str, advice_price: float, category: str, available: bool):
        self.id = id
        self.title = title
        self.advice_price = advice_price
        self.category = category
        self.available = available
        self.db_conn = sqlite3.connect("shop.db")
      

    def get_ratings(self) -> list:
        rows = self.db_conn.execute("SELECT rating FROM ratings WHERE product_id = ? ", [self.id])
        ratings = rows.fetchall()
        ratings_list = []

        for rating in ratings:
            rating.append(ratings_list)

        return ratings_list        
    
    def get_purchases(self) -> list:
        rows = self.db_conn.execute("SELECT amount FROM purchases WHERE product_id = ?", [self.id])
        purchases = rows.fetchall()
        purchase_list = []

        for purchase in purchases:
            purchase.append(purchase_list)
        
        return purchase_list

      # Representation method
    # This will format the output in the correct order
    # Format is @dataclass-style: Classname(attr=value, attr2=value2, ...)
    def __repr__(self) -> str:
        sorted_items = sorted(self.__dict__.items(), key=lambda item: item[0])
        return "{}({})".format(
            type(self).__name__,
            ", ".join([f"{key}={value!s}" for key, value in sorted_items]),
        )

    
    