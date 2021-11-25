import plenty.models as models
from datetime import datetime, timedelta


async def plenty_liquidity_change_percentage_hours(liquidity_plenty_dollar, amount_hours):
    timestamp_now = datetime.utcnow()
    timestamp_hours_ago = timestamp_now - timedelta(hours=amount_hours)

    plenty_lp_stats = await models.PlentyStats \
        .filter(timestamp__gte=timestamp_hours_ago) \
        .filter(timestamp__lte=timestamp_now) \
        .order_by("timestamp") \
        .first()

    try:
        liquidity_plenty_hours_ago = plenty_lp_stats.liquidity
        liquidity_change_token = ((liquidity_plenty_dollar - liquidity_plenty_hours_ago) / liquidity_plenty_hours_ago) * 100
    except (TypeError, AttributeError):
        liquidity_change_token = 0


    return liquidity_change_token