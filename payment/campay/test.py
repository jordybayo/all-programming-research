from campay.sdk import Client

campay = Client({
    "app_username" : "221zjdYJX8eHIsAuzgEQsg-e3rFPsQsgGUToggD0ww8qBqLd7elPjucxk5rD5Nisa4mGohIuYjdydDbAF_ceTQ",
    "app_password" : "xiGy3yzBC26opUDBOHuwEOAh-NHzlZUBThwD1IRNNG_M99RoZaB5YUFWOaTfMZCc8fCWAsW6FrAguEQ6z03NHw",
    "environment" : "DEV" #use "DEV" for demo mode or "PROD" for live mode
})

balance = campay.get_balance()

print(balance)
#{"total_balance": 0, "mtn_balance": 0, "orange_balance": 0, "currency": "XAF"}

collect = campay.collect({
    "amount": "5", #The amount you want to collect
    "currency": "XAF",
    "from": "237695113844", #Phone number to request amount from. Must include country code
    "description": "buy on wivroo"
})

