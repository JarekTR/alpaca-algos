import alpaca_trade_api as trade_api
from config import *


def get_account(api):
    account = api.get_account()
    return account


def get_quotes(data_api):
    return data_api.get_quotes("AAPL", "2021-02-08", "2021-02-08", limit=10).df


def get_trades(data_api):
    return data_api.get_trades("AAPL", "2021-02-08", "2021-02-08", limit=10).df


def buy_order(api):
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


def sell_order(api):
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


api = trade_api.REST(API_KEY, SECRET_KEY, APCA_API_BASE_URL)
data_api = trade_api.REST(API_KEY, SECRET_KEY, APCA_API_DATA_URL)


test_account = get_account(api)
test_quotes = get_quotes(data_api)
test_trades = get_trades(data_api)
test_buy = buy_order(api)
test_sell = sell_order(api)

print(test_account, "\n")
print(test_quotes, "\n")
print(test_trades, "\n")
print(test_buy, "\n")
print(test_sell)
