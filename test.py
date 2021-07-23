import alpaca_trade_api as trade_api
from config import *


def get_account():
    api = trade_api.REST(API_KEY, SECRET_KEY, APCA_API_BASE_URL)
    account = api.get_account()
    return account


def get_quotes():
    api = trade_api.REST(API_KEY, SECRET_KEY, APCA_API_DATA_URL)
    return api.get_quotes("AAPL", "2021-02-08", "2021-02-08", limit=10).df


def buy_order():
    api = trade_api.REST(API_KEY, SECRET_KEY, APCA_API_BASE_URL)
    order = api.submit_order(
        "AAPL",
        qty=5,
        side="buy",
        type="market",
        time_in_force="day",
        limit_price=None,
        stop_price=None,
        client_order_id=None,
        order_class=None,
        take_profit=None,
        stop_loss=None,
        trail_price=None,
        trail_percent=None,
        notional=None,
    )
    return order

def sell_order():
    api = trade_api.REST(API_KEY, SECRET_KEY, APCA_API_BASE_URL)
    order = api.submit_order(
        "AAPL",
        qty=5,
        side="sell",
        type="market",
        time_in_force="day",
        limit_price=None,
        stop_price=None,
        client_order_id=None,
        order_class=None,
        take_profit=None,
        stop_loss=None,
        trail_price=None,
        trail_percent=None,
        notional=None,
    )
    return order


test_account = get_account()
test_quotes = get_quotes()
test_buy = buy_order()
test_sell = sell_order()

print(test_account, "\n")
print(test_quotes, "\n")
print(test_buy, "\n")
print(test_sell)
