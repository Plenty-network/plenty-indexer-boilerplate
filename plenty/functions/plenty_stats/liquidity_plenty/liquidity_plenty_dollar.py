import plenty.models as models
from decimal import Decimal


async def liquidity_plenty_dollar(symbol_2, plenty_price_dollars):
    latest_lp_trade = await models.Position \
        .filter(symbol_1="PLENTY", symbol_2=symbol_2) \
        .order_by("-timestamp") \
        .first()

    plenty_pool = latest_lp_trade.quantity_pool1

    result = Decimal(plenty_pool * plenty_price_dollars)

    return result
