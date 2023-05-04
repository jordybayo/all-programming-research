from sdk_2 import Client
from sdk_2 import status_list
import multiprocessing
from threading import Thread
import time
import asyncio

def payment():
    client =  Client({
        "app_username" : "221zjdYJX8eHIsAuzgEQsg-e3rFPsQsgGUToggD0ww8qBqLd7elPjucxk5rD5Nisa4mGohIuYjdydDbAF_ceTQ",
        "app_password" : "xiGy3yzBC26opUDBOHuwEOAh-NHzlZUBThwD1IRNNG_M99RoZaB5YUFWOaTfMZCc8fCWAsW6FrAguEQ6z03NHw",
        "environment" : "DEV" #use "DEV" for demo mode or "PROD" for live mode
    })
    print('tim')
    asyncio.create_task(client.collect({
        "amount": "5", #The amount you want to collect
        "currency": "XAF",
        "from": "237656714050", #Phone number to request amount from. Must include country code
        "description": "buy on wivroo"
    }))
    print('finished')

def verification_des_state():
    if 'FAILED' in status_list[-1]:
        print(">> nous avons echoue")
    elif 'SUCCESSFUL ' in status_list[-1]:
        print(">> nous avons reusi")
    elif  'collecting' in status_list[-1]:
        print(">> nous avons initiez le paiement") 
    elif 'confirm' in status_list[-1]:
        print(">> nous avons initiez le paiement") 
    else:
        print(">> nous avons echoueee")

asyncio.run(payment)

finish = time.perf_counter()
print('Finished running after seconds: ', finish)