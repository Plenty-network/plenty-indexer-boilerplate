import plenty.models as models
from datetime import datetime, timedelta
from decimal import Decimal


async def plenty_volume_change_percentage_hours(volume_plenty_dollar_24hours, amount_hours):
    timestamp_now = datetime.utcnow()
    timestamp_hours_ago = timestamp_now - timedelta(hours=amount_hours)

    plenty_day_stats = await models.PlentyStats \
        .filter(timestamp__gte=timestamp_hours_ago) \
        .filter(timestamp__lte=timestamp_now) \
        .order_by("timestamp") \
        .first()

    try:
        volume_plenty_hours_ago = plenty_day_stats.volume_token
        volume_change_plenty = Decimal(((volume_plenty_dollar_24hours - volume_plenty_hours_ago) / volume_plenty_hours_ago) * 100)
    except (TypeError, AttributeError):
        volume_change_plenty = Decimal(1)

    return volume_change_plenty
