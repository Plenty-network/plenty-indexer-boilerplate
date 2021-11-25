import plenty.models as models

async def block_level(symbol_plenty):
    # latest trade amm
    trade_token = await models.Trade \
        .filter(symbol_1=symbol_plenty) \
        .order_by("-timestamp") \
        .first()

    # set side information token
    level_token = trade_token.level

    return level_token