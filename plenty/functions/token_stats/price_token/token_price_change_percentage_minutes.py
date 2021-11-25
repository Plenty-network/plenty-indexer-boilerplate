import plenty.models as models
from decimal import Decimal
from datetime import datetime, timedelta


async def token_price_change_percentage_minutes(symbol_token, price_token_dollar, amount_minutes):
    timestamp_now = datetime.utcnow()
    timestamp_minutes_ago = timestamp_now - timedelta(minutes=amount_minutes)

    token_day_stats = await models.TokenStats \
        .filter(symbol_token=symbol_token) \
        .filter(timestamp__gte=timestamp_minutes_ago) \
        .filter(timestamp__lte=timestamp_now) \
        .order_by("timestamp") \
        .first()

    try:
        price_token_minutes_ago = token_day_stats.token_price
        price_change_token = Decimal(((price_token_dollar - price_token_minutes_ago) / price_token_minutes_ago) * 100)
    except (TypeError, AttributeError):
        price_change_token = Decimal(1)

    return price_change_token
