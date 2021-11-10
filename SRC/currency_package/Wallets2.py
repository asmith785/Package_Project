# %%

class WalletEuro:
    coversion_rates = {"usd" :1.16, "gbp": 0.86, "yen": 131.79, "franc": 1.06}
#shows euro conversion rates for each each currency starting at $1

    def __init__(self,currency_amount):
        self.currency_amount = currency_amount
        self.currency_type = "euro"

    def convert_currency(self,currency_type):
        conversion_rate = WalletEuro.coversion_rates[currency_type]
        converted_amount = self.currency_amount * conversion_rate
        return converted_amount


class WalletYen:
    coversion_rates = {"usd" :0.088, "euro": 0.0076, "gbp": 0.0064, "franc": 0.0081 }
#shows yen conversion rates for each each currency starting at $1


    def __init__(self,currency_amount):
        self.currency_amount = currency_amount
        self.currency_type = "yen"

    def convert_currency(self,currency_type):
        conversion_rate = WalletYen.coversion_rates[currency_type]
        converted_amount = self.currency_amount * conversion_rate
        return converted_amount


# TODO Updating conversion rate function


# %%
