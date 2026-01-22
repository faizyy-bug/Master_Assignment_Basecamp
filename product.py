import sqlite3


class Product:
    def __init__(self, id: int, title: str, advice_price: float, category: str, available: bool):
        self.id = id
        self.title = title
        self.advice_price = advice_price
        self.category = category
        self.available = available
      

    def get_ratings(self) -> list:
        from rating import Rating
        with sqlite3.connect("shop.db") as db_conn:

            rows = db_conn.execute("SELECT id, product_id, rating, minimum_value_scale, maximum_value_scale FROM ratings WHERE product_id = ? ", [self.id]).fetchall()
            ratings_list = []

            for row in rows:
                ratings_list.append(Rating(id=row[0], maximum_value_scale=row[4], minimum_value_scale=row[3], product_id=row[1], rating=row[2]))

        return ratings_list        
    

    def get_purchases(self) -> list:
        from purchase import Purchase
        with sqlite3.connect("shop.db") as db_conn:

            rows = db_conn.execute("SELECT id, product_id, amount, currency, price_per_unit, purchase_date FROM purchases WHERE product_id = ?", [self.id]).fetchall()
            purchase_list = []

            for purchase in rows:
                purchase_list.append(Purchase(id= purchase[0], product_id= purchase[1], amount= purchase[2], currency= purchase[3], price_per_unit= purchase[4], purchase_datetime= purchase[5]))

        return purchase_list

    def __repr__(self) -> str:
        sorted_items = sorted(self.__dict__.items(), key=lambda item: item[0])
        return "{}({})".format(
            type(self).__name__,
            ", ".join([f"{key}={value!s}" for key, value in sorted_items]),
        )

    