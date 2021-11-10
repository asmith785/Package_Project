# %%
import Wallets
import Wallets2
import Swiss_Wallet

# questions to ask user
def create_wallet():
    currency_type = input("What is your current currency : usd, gbp, euro, yen, franc?")
    currency_amount = float(input("What is your currency amount?"))


# grabs from imported wallet to get currency value
    if currency_type == "usd":
        wallet = Wallets.WalletUSD(currency_amount)
    elif currency_type == "gbp":
        wallet = Wallets.WalletGBP(currency_amount)
    elif currency_type == "euro":
        wallet = Wallets2.WalletEuro(currency_amount)
    elif currency_type == "yen":
        wallet = Wallets2.WalletYen(currency_amount)
    elif currency_type == "franc":
        wallet = Swiss_Wallet.WalletSwiss(currency_amount)
    else:
        print("invalid currency type")
    return wallet



#TODO add validation
#TODO backend from userInterface
#TODO update amount left in wallet class method done in wallet.py
# %%
