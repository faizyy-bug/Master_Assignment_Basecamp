import os
import sys
import csv

from currency_exchange import CurrencyExchange
from rating import Rating
from datetime import datetime
from product import Product


class Reporter:
    # 1 how many products are there? -> int
    def total_amount_of_products(self) -> int:
        raise NotImplementedError()

    # 2 What is the most rated product? -> Product
    def most_rated_product(self):
        raise NotImplementedError()

    # 3 how often is a product bought? -> int
    def how_often_is_a_product_bought(self, product_id: int) -> int:
        raise NotImplementedError()

    # 4 give a list of the currencies sorted by most used to least used -> list[str]
    def currencies_by_usage(self) -> list[str]:
        raise NotImplementedError()

    # 5 what is the average price a product is sold for in USD? -> float
    # 6 what is the average price a product is sold for in a given currency? -> float
    def average_price_of_product_in_currency(
        self, product_id: int, currency: str = "USD"
    ) -> float | None:
        raise NotImplementedError()

    # 7 Give a list of potential available presents for a given budget in a given currency for the advice price and in a given category. Take the top 5 sorted by rating.
    def potential_presents(
        self, min_budget: float, max_budget: float, currency: str, category: str
    ) -> list[Product]:
        raise NotImplementedError()

    # 8 What is the average rating of a product on a scale from 1 to 5? -> float
    def average_rating_of_product(self, product_id: int) -> float | None:
        raise NotImplementedError()

    # 9 What is the average rating of a product on a given scale
    def average_rating_of_product_in_scale(
        self, product_id: int, new_minimum: int, new_maximum: int
    ) -> float | None:
        raise NotImplementedError()

    # 10 report the products that are out of stock -> list[Product]
    def products_out_of_stock(self) -> list[Product]:
        raise NotImplementedError()

    # 11 report the products in a category with their name, advice price and rating based on a scale from 1 to 5
    def products_in_category(self, category: str, to_csv: bool = False) -> list[tuple]:
        raise NotImplementedError()

    # 12 report the product in a category that are sold between x and y date.
    # report there name, advice price, and average price sold for in USD and how many were sold in that period.
    def products_sold_in_period(
        self,
        category: str,
        start_date: datetime,
        end_date: datetime,
        to_csv: bool = False,
    ) -> list[tuple]:
        raise NotImplementedError()
