import plenty.models as models
from decimal import Decimal

async def plenty_price_dollar(symbol_plenty):
    trade_wusdc = await models.Trade \
        .filter(symbol_1=symbol_plenty, symbol_2="wUSDC") \
        .order_by("-timestamp") \
        .first()

    trade_wbusd = await models.Trade \
        .filter(symbol_1=symbol_plenty, symbol_2="wBUSD") \
        .order_by("-timestamp") \
        .first()

    try:
        price_wusdc_plenty = Decimal(trade_wusdc.price)
        price_wbusd_plenty = Decimal(trade_wbusd.price)
        price_plenty_dollar = Decimal((price_wusdc_plenty + price_wbusd_plenty) / 2)
    except (TypeError, AttributeError):
        price_plenty_dollar = Decimal(1)

    return price_plenty_dollar