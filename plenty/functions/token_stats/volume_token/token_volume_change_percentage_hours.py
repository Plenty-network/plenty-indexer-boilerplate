import plenty.models as models
from datetime import datetime, timedelta
from decimal import Decimal


async def token_volume_change_percentage_hours(symbol_token, volume_token_dollar, amount_hours):
    timestamp_now = datetime.utcnow()
    timestamp_hours_ago = timestamp_now - timedelta(hours=amount_hours)

    token_day_stats = await models.TokenStats \
        .filter(symbol_token=symbol_token) \
        .filter(timestamp__gte=timestamp_hours_ago) \
        .filter(timestamp__lte=timestamp_now) \
        .order_by("timestamp") \
        .first()

    try:
        volume_token_hours_ago = token_day_stats.volume_token
        volume_change_token = Decimal((volume_token_dollar - volume_token_hours_ago) / volume_token_hours_ago) * 100
    except (TypeError, AttributeError):
        volume_change_token = Decimal(1)

    return volume_change_token
