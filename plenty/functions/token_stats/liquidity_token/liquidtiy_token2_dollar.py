import plenty.models as models
from decimal import Decimal


async def liquidtiy_token2_dollar(symbol_1, symbol_2):
    token_stats = await models.TokenStats \
        .filter(symbol_token=symbol_2) \
        .order_by("-timestamp") \
        .first()

    try:
        token_price = token_stats.token_price

        latest_lp_trade = await models.Position \
            .filter(symbol_1=symbol_1, symbol_2=symbol_2) \
            .order_by("-timestamp") \
            .first()

        token_pool = latest_lp_trade.quantity_pool2
        liquidity_token_dollar = Decimal(token_pool * token_price)
    except (TypeError, AttributeError):
        liquidity_token_dollar = Decimal(1)

    return liquidity_token_dollar
