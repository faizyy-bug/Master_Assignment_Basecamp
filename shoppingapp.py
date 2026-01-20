import sqlite3
import json
from shopreporter import Reporter


def convert_to_db(file : str):
    db_conn = sqlite3.connect("shop.db")
    cur = db_conn.cursor()

    cur.execute("DELETE FROM products")
    cur.execute("DELETE FROM purchases")
    cur.execute("DELETE FROM ratings")
    db_conn.commit()

    with open(file, "r") as f:
        data = json.load(f)
    
    
    for product in data:
    
        product_title = product["title"]
        product_advice = product["advice_price"]
        product_category = product["category"]
        product_available = product["available"]
        product_rating = product["ratings"]
        product_purchase = product["purchases"]
        product_id = product["id"]
        product_base = db_conn.execute("""INSERT INTO products (id, title, advice_price, category, available)
                                   VALUES (?, ?, ?, ?, ?)""",
                                   [product_id, product_title, product_advice, product_category, product_available])
        db_conn.commit()

        for r in product_rating:

            sub_id = r["id"]
            sub_scale_split = r["scale"].split("-")
            sub_scale_min = sub_scale_split[0]
            sub_scale_max = sub_scale_split[1]
            sub_rating = r["rating"]
            ratings_base = db_conn.execute("""INSERT INTO ratings(id, product_id, rating, minimum_value_scale, maximum_value_scale)
                                   VALUES (?, ?, ?, ?, ?)""",
                                   [sub_id, product_id, sub_rating, sub_scale_min, sub_scale_max])
            db_conn.commit()
        for p in product_purchase:
                purchase_id = p["id"]
                purchase_amount = p["amount"]
                purchase_currency = p["currency"]
                purchase_ppu = p["price_per_unit"]
                purchase_date = p["date_time"] + "00:00:00"
                purchase_base = db_conn.execute("""INSERT INTO purchases 
                                   (id, product_id, amount, currency, purchase_date, price_per_unit)
                                   VALUES (?, ?, ?, ?, ?, ? )""", 
                                   [purchase_id, product_id, purchase_amount, purchase_currency, purchase_date, purchase_ppu])
                db_conn.commit()



def main() -> None:
    filename = "products.json"
    convert_to_db(filename)
    report = Reporter()

    print(report.total_amount_of_products())



    



if __name__ == "__main__":
    main()

