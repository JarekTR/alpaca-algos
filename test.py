import json
import requests
from config import *


def get_account():
    r = requests.get(ACCOUNT_URL, headers=HEADERS)
    return json.loads(r.content)


def create_order(symbol, qty, side, type, time_in_force):
    data = {
        "symbol": symbol,
        "qty": qty,
        "side": side,
        "type": type,
        "time_in_force": time_in_force,
    }
    r = requests.post(ORDER_URL, json=data, headers=HEADERS)
    return json.loads(r.content)


test_account = get_account()
test_buy = create_order("AAPL", 5, "buy", "market", "gtc")
test_sell = create_order("AAPL", 5, "sell", "market", "gtc")

print(test_account, "\n")
print(test_buy, "\n")
print(test_sell)
