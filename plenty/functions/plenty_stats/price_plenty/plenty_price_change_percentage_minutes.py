import plenty.models as models
from decimal import Decimal
from datetime import datetime, timedelta


async def plenty_price_change_percentage_minutes(price_plenty_dollar, amount_minutes):
    timestamp_now = datetime.utcnow()
    timestamp_past = timestamp_now - timedelta(minutes=amount_minutes)

    plenty_day_stats = await models.PlentyStats \
        .filter(timestamp__gte=timestamp_past) \
        .filter(timestamp__lte=timestamp_now) \
        .order_by("timestamp") \
        .first()

    try:
        price_token_past = plenty_day_stats.price
        price_change_plenty = Decimal(((price_plenty_dollar - price_token_past) / price_token_past) * 100)
    except (TypeError, AttributeError):
        price_change_plenty = Decimal(1)

    return price_change_plenty
