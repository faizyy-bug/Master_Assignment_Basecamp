class CurrencyExchange():

    def convert(self, amount: float, from_currency: str, to_currency: str) -> float | None:

        with open("currencies.csv", "r") as file:
            next(file)

            for line in file:
        
                currency_country, currency_rate = line.strip().split(",")
                currency_rate = float(currency_rate)

                if currency_country == from_currency:
                    from_rate = currency_rate

                elif currency_country == to_currency:
                    to_rate = currency_rate

            if from_rate is None or to_rate is None:
                return None
                
            return float(amount * (to_rate / from_rate))
    