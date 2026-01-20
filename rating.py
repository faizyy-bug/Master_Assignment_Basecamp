import sqlite3
from product import Product

class Rating:
    def __init__(self, id: int, product_id: int, rating: int, minimum_value_scale: int, maximum_value_scale: int):
        self.id = id
        self.product_id = product_id
        self.rating = rating
        self.min_value = minimum_value_scale
        self.max_value = maximum_value_scale
        self.db_conn = sqlite3.connect("shop.db")
    
    def get_product(self) -> Product:
        cur = self.db_conn.cursor()
        cur.execute("SELECT title, advice_price, category, available FROM products WHERE id = ? ", [self.product_id])
        product_row = cur.fetchone()
        return Product(*product_row)
    
    def get_normalized_rating(self) -> float:
        return  float(self.rating - self.min_value) / (self.max_value - self.min_value)

    def get_rating_in_scale(self, new_minimum: int, new_maximum: int) -> float:
        normalized_rating = self.get_normalized_rating()
        calculation = normalized_rating * (new_maximum - new_minimum) + (new_minimum)

        return float(calculation)
    
    def is_rating_higher_than(self, other) -> bool:
        if self.rating > other.rating:
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