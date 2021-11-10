# %%
import Wallets
import Wallets2
import Swiss_Wallet

def create_wallet():
    currency_type = input("What is your current currency : usd, gbp, euro, yen, franc?")
    currency_amount = float(input("What is your currency amount?"))
    #converted_type = input("what currency you would like to convert too: usd, gpd, euro, yen?")

#TODO add validation
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

#___ = create_wallet() to start
#____.coverted_type(_)

#backend from userInterface
#TODO update amount left in wallet class method done in wallet.py
# usd to pound
# %%
