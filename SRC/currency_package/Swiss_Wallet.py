# %%
class WalletSwiss:
    coversion_rates = {"usd" :1.10, "gpd": 0.81, "euro": 0.95, "yen": 123.84 }

    def __init__(self,currency_amount):
        self.currency_amount = currency_amount
        self.currency_type = "franc"

    def convert_currency(self,currency_type):
        conversion_rate = WalletSwiss.coversion_rates[currency_type]
        converted_amount = self.currency_amount * conversion_rate
        return converted_amount





# TODO Updating conversion rate function
# %%
