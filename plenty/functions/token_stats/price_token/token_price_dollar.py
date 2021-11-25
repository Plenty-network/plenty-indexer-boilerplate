import plenty.models as models
from decimal import Decimal


async def token_price_dollar(symbol_1, symbol_2):
    plenty_stats = await models.PlentyStats \
        .filter(symbol_plenty="PLENTY") \
        .order_by("-timestamp") \
        .first()

    try:
        plenty_price = plenty_stats.price

        trade_token = await models.Trade \
            .filter(symbol_1=symbol_1, symbol_2=symbol_2) \
            .order_by("-timestamp") \
            .first()

        price_token_plenty = trade_token.price
        price_token_dollar = Decimal((1 / price_token_plenty) * plenty_price)
    except (TypeError, AttributeError):
        price_token_dollar = Decimal(1)

    return price_token_dollar
