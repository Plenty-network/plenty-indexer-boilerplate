import plenty.models as models
from decimal import Decimal


async def token_price_dollar_without_plenty(symbol_1, symbol_2):
    try:
        trade_token = await models.Trade \
            .filter(symbol_1=symbol_1, symbol_2=symbol_2) \
            .order_by("-timestamp") \
            .first()

        quantity_tk1 = trade_token.quantity_tk1
        quantity_tk2 = trade_token.quantity_tk2
        price_token_dollar = Decimal(quantity_tk1 / quantity_tk2)

    except (TypeError, AttributeError):
        price_token_dollar = Decimal(1)

    return price_token_dollar
