import plenty.models as models
from decimal import Decimal
from datetime import datetime, timedelta


async def token_price_change_percentage_hours(symbol_token, price_token_dollar, amount_hours):
    timestamp_now = datetime.utcnow()
    timestamp_hours_ago = timestamp_now - timedelta(hours=amount_hours)

    token_day_stats = await models.TokenStats \
        .filter(symbol_token=symbol_token) \
        .filter(timestamp__gte=timestamp_hours_ago) \
        .filter(timestamp__lte=timestamp_now) \
        .order_by("timestamp") \
        .first()

    try:
        price_token_hours_ago = token_day_stats.token_price
        price_change_token = Decimal(((price_token_dollar - price_token_hours_ago) / price_token_hours_ago) * 100)
    except (TypeError, AttributeError):
        price_change_token = Decimal(1)

    return price_change_token
