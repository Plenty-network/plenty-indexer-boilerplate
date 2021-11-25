import plenty.models as models
from decimal import Decimal
from datetime import datetime, timedelta


async def plenty_price_change_percentage_24hours(symbol_plenty, price_plenty_dollar):
    timestamp_now = datetime.utcnow()
    timestamp_yesterday = timestamp_now - timedelta(hours=24)

    plenty_day_stats = await models.PlentyStats \
        .filter(symbol_plenty=symbol_plenty) \
        .filter(timestamp__gte=timestamp_yesterday) \
        .filter(timestamp__lte=timestamp_now) \
        .order_by("timestamp") \
        .first()

    price_token_day_ago = plenty_day_stats.price
    price_change_plenty = Decimal(((price_plenty_dollar - price_token_day_ago) / price_token_day_ago) * 100)

    return price_change_plenty
