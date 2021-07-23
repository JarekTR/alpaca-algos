import alpaca_trade_api as alpaca
from config import *


def get_account(trade_api):
    account = trade_api.get_account()
    return account


def get_quotes(data_api):
    return data_api.get_quotes("AAPL", "2021-02-08", "2021-02-08", limit=10).df


def get_trades(data_api):
    return data_api.get_trades("AAPL", "2021-02-08", "2021-02-08", limit=10).df


def buy_order(trade_api):
    order = trade_api.submit_order(
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


def sell_order(trade_api):
    order = trade_api.submit_order(
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


trade_api = alpaca.REST(API_KEY, SECRET_KEY, APCA_API_BASE_URL)
data_api = alpaca.REST(API_KEY, SECRET_KEY, APCA_API_DATA_URL)


test_buy = buy_order(trade_api)
test_account = get_account(trade_api)
test_quotes = get_quotes(data_api)
test_trades = get_trades(data_api)
test_sell = sell_order(trade_api)


print(test_account, "\n")
print(test_quotes, "\n")
print(test_trades, "\n")
print(test_buy, "\n")
print(test_sell)
