import plenty.models as models
from datetime import datetime, timedelta
from decimal import Decimal


async def plenty_volume_change_percentage_weeks(volume_plenty_dollar_24hours, amount_weeks):
    timestamp_now = datetime.utcnow()
    timestamp_weeks_ago = timestamp_now - timedelta(weeks=amount_weeks)

    plenty_stats = await models.PlentyStats \
        .filter(timestamp__gte=timestamp_weeks_ago) \
        .filter(timestamp__lte=timestamp_now) \
        .order_by("timestamp") \
        .first()

    try:
        volume_plenty_weeks_ago = plenty_stats.volume_token
        volume_change_plenty = ((volume_plenty_dollar_24hours - volume_plenty_weeks_ago) / volume_plenty_weeks_ago) * 100
    except (TypeError, AttributeError):
        volume_change_plenty = Decimal(1)

    return volume_change_plenty
