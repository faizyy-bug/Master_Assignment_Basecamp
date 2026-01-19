import sqlite3

class Rating:
    def __init__(self, id: int, product_id: int, rating: int, minimum_value_scale: int, maximum_value_scale: int):
        self.id = id
        self.product_id = product_id
        self.rating = rating
        self.min_value = minimum_value_scale
        self.max_value = maximum_value_scale
        self.db_conn = sqlite3.connect("shop.db")
    
    def 


      # Representation method
    # This will format the output in the correct order
    # Format is @dataclass-style: Classname(attr=value, attr2=value2, ...)
    def __repr__(self) -> str:
        sorted_items = sorted(self.__dict__.items(), key=lambda item: item[0])
        return "{}({})".format(
            type(self).__name__,
            ", ".join([f"{key}={value!s}" for key, value in sorted_items]),
        )