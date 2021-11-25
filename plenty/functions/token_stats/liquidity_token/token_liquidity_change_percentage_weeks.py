import plenty.models as models
from datetime import datetime, timedelta
from decimal import Decimal


async def token_liquidity_change_percentage_weeks(symbol_token, liquidity_token_dollar, amount_weeks):
    timestamp_now = datetime.utcnow()
    timestamp_weeks_ago = timestamp_now - timedelta(weeks=amount_weeks)

    token_lp_stats = await models.TokenStats \
        .filter(symbol_token=symbol_token) \
        .filter(timestamp__gte=timestamp_weeks_ago) \
        .filter(timestamp__lte=timestamp_now) \
        .order_by("timestamp") \
        .first()

    try:
        liquidity_token_weeks_ago = token_lp_stats.liquidity
        liquidity_change_token = Decimal(((liquidity_token_dollar - liquidity_token_weeks_ago) / liquidity_token_weeks_ago) * 100)
    except (TypeError, AttributeError):
        liquidity_change_token = Decimal(1)

    return liquidity_change_token
