import plenty.models as models
from decimal import Decimal
from datetime import datetime, timedelta


async def volume_token1_dollar_24hours(symbol_1, symbol_2):
    timestamp_now = datetime.utcnow()
    timestamp_yesterday = timestamp_now - timedelta(hours=24)

    token_stats = await models.TokenStats \
        .filter(symbol_token=symbol_1) \
        .order_by("-timestamp") \
        .first()

    try:
        token_price = token_stats.token_price

        token_day_trades = await models.Trade \
            .filter(symbol_1=symbol_1, symbol_2=symbol_2) \
            .filter(timestamp__gte=timestamp_yesterday) \
            .filter(timestamp__lte=timestamp_now) \

        trades_token_range = len(token_day_trades)
        volume_token = Decimal(0)

        for i in range(trades_token_range):
            volume_token = volume_token + token_day_trades[i].quantity_tk1

        volume_token1_dollar = Decimal(volume_token * token_price)
    except (TypeError, AttributeError):
        volume_token1_dollar = Decimal(1)

    return volume_token1_dollar
