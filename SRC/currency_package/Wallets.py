# %%

class WalletUSD:
    coversion_rates = {"gbp" :0.73, "euro": 0.86, "yen": 113.94 , "franc": 0.91}

    def __init__(self,currency_amount):
        self.currency_amount = currency_amount
        self.currency_type = "usd"

    def convert_currency(self,currency_type):
        conversion_rate = WalletUSD.coversion_rates[currency_type]
        converted_amount = self.currency_amount * conversion_rate
        return converted_amount


class WalletGBP:
    coversion_rates = {"usd" :1.36, "euro": 1.18, "yen": 155.98, "franc": 1.24 }

    def __init__(self,currency_amount):
        self.currency_amount = currency_amount
        self.currency_type = "gbp"

    def convert_currency(self,currency_type):
        conversion_rate = WalletGBP.coversion_rates[currency_type]
        converted_amount = self.currency_amount * conversion_rate
        return converted_amount

# TODO Updating conversion rate function






# %%
