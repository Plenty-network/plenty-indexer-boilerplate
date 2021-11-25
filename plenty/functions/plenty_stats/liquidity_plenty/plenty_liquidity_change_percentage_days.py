import plenty.models as models
from datetime import datetime, timedelta


async def plenty_liquidity_change_percentage_days(liquidity_plenty_dollar, amount_days):
    timestamp_now = datetime.utcnow()
    timestamp_days_ago = timestamp_now - timedelta(days=amount_days)

    plenty_lp_stats = await models.PlentyStats \
        .filter(timestamp__gte=timestamp_days_ago) \
        .filter(timestamp__lte=timestamp_now) \
        .order_by("timestamp") \
        .first()

    try:
        liquidity_plenty_days_ago = plenty_lp_stats.liquidity
        liquidity_change_token = ((liquidity_plenty_dollar - liquidity_plenty_days_ago) / liquidity_plenty_days_ago) * 100
    except (TypeError, AttributeError):
        liquidity_change_token = 0


    return liquidity_change_token