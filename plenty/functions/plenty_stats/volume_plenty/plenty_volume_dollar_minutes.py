import plenty.models as models
from decimal import Decimal
from datetime import datetime, timedelta


async def plenty_volume_dollar_minutes(symbol_1, price_plenty_dollar, amount_minutes):
    timestamp_now = datetime.utcnow()
    timestamp_minutes_ago = timestamp_now - timedelta(minutes=amount_minutes)

    plenty_day_trades = await models.Trade \
        .filter(symbol_1=symbol_1) \
        .filter(timestamp__gte=timestamp_minutes_ago) \
        .filter(timestamp__lte=timestamp_now) \

    try:
        trades_token_range = len(plenty_day_trades)
        volume_token = 0

        for i in range(trades_token_range):
            volume_token = volume_token + plenty_day_trades[i].quantity_tk1

        volume_plenty_dollar = Decimal(volume_token * price_plenty_dollar)
    except (TypeError, AttributeError):
        volume_plenty_dollar = Decimal(1)

    return volume_plenty_dollar
