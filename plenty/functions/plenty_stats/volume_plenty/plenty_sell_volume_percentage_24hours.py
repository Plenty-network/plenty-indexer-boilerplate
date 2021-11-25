import plenty.models as models
from datetime import datetime, timedelta
from decimal import Decimal


async def plenty_sell_volume_percentage_24hours(symbol_plenty, plenty_price_dollar, plenty_volume_dollar_24hours):
    timestamp_now = datetime.utcnow()
    timestamp_yesterday = timestamp_now - timedelta(hours=24)

    plenty_day_trades = await models.Trade \
        .filter(symbol_1=symbol_plenty) \
        .filter(timestamp__gte=timestamp_yesterday) \
        .filter(timestamp__lte=timestamp_now) \
        .filter(side_trade=1)

    try:
        trades_token_range = len(plenty_day_trades)
        sell_volume_token = 0

        for i in range(trades_token_range):
            sell_volume_token = sell_volume_token + plenty_day_trades[i].quantity_tk1

        sell_volume_plenty_dollar = Decimal(sell_volume_token * plenty_price_dollar)
        buy_volume_percentage = Decimal((sell_volume_plenty_dollar / plenty_volume_dollar_24hours) * 100)
    except (TypeError, AttributeError):
        buy_volume_percentage = Decimal(1)

    return buy_volume_percentage
