import plenty.models as models
from decimal import Decimal
from datetime import datetime, timedelta


async def token_price_change_percentage_weeks(symbol_token, price_token_dollar, amount_weeks):
    timestamp_now = datetime.utcnow()
    timestamp_weeks_ago = timestamp_now - timedelta(weeks=amount_weeks)

    token_day_stats = await models.TokenStats \
        .filter(symbol_token=symbol_token) \
        .filter(timestamp__gte=timestamp_weeks_ago) \
        .filter(timestamp__lte=timestamp_now) \
        .order_by("timestamp") \
        .first()

    try:
        price_token_weeks_ago = token_day_stats.token_price
        price_change_token = Decimal(((price_token_dollar - price_token_weeks_ago) / price_token_weeks_ago) * 100)
    except (TypeError, AttributeError):
        price_change_token = Decimal(1)

    return price_change_token
