from datetime import datetime
import plenty.models as models
from dipdup.context import HookContext

from plenty.functions.block_level import block_level
from plenty.functions.plenty_stats.liquidity_plenty.liquidity_plenty_dollar import liquidity_plenty_dollar
from plenty.functions.plenty_stats.liquidity_plenty.plenty_liquidity_change_percentage_days import plenty_liquidity_change_percentage_days
from plenty.functions.plenty_stats.volume_plenty.plenty_buy_volume_percentage_24hours import plenty_buy_volume_percentage_24hours
from plenty.functions.plenty_stats.price_plenty.plenty_price_dollar import plenty_price_dollar
from plenty.functions.plenty_stats.volume_plenty.plenty_sell_volume_percentage_24hours import plenty_sell_volume_percentage_24hours
from plenty.functions.plenty_stats.volume_plenty.plenty_volume_change_percentage_hours import plenty_volume_change_percentage_hours
from plenty.functions.plenty_stats.volume_plenty.plenty_volume_dollar_days import plenty_volume_dollar_days
from plenty.functions.plenty_stats.price_plenty.plenty_price_change_percentage_hours import plenty_price_change_percentage_hours


async def calculate_plenty_stats(
        ctx: HookContext,
        major: bool,
) -> None:
    timestamp_now = datetime.utcnow()
    symbol_plenty = "PLENTY"
    level_block = await block_level(symbol_plenty)

    price_plenty_dollar = await plenty_price_dollar(symbol_plenty)
    price_change_plenty = await plenty_price_change_percentage_hours(price_plenty_dollar, 24)

    volume_plenty_dollar = await plenty_volume_dollar_days(symbol_plenty, price_plenty_dollar, 1)
    volume_change_plenty = await plenty_volume_change_percentage_hours(volume_plenty_dollar, 24)

    # buy_volume_plenty_percentage = await plenty_buy_volume_percentage_24hours(symbol_plenty, price_plenty_dollar, volume_plenty_dollar)
    # sell_volume_plenty_percentage = await plenty_sell_volume_percentage_24hours(symbol_plenty, price_plenty_dollar, volume_plenty_dollar)
    #
    # print("sell:", " ", sell_volume_plenty_percentage)
    # print("buy:", " ", buy_volume_plenty_percentage)

    # calculation liquidity_token plenty token
    plenty_ctez = await liquidity_plenty_dollar("ctez", price_plenty_dollar)
    plenty_wbusd = await liquidity_plenty_dollar("wBUSD", price_plenty_dollar)
    plenty_wusdc = await liquidity_plenty_dollar("wUSDC", price_plenty_dollar)
    plenty_wwbtc = await liquidity_plenty_dollar("wWBTC", price_plenty_dollar)
    plenty_wmatic = await liquidity_plenty_dollar("wMATIC", price_plenty_dollar)
    plenty_wlink = await liquidity_plenty_dollar("wLINK", price_plenty_dollar)
    plenty_usdtz = await liquidity_plenty_dollar("USDtz", price_plenty_dollar)
    plenty_hdao = await liquidity_plenty_dollar("hDAO", price_plenty_dollar)
    plenty_wweth = await liquidity_plenty_dollar("wWETH", price_plenty_dollar)
    plenty_kusd = await liquidity_plenty_dollar("kUSD", price_plenty_dollar)
    plenty_quipu = await liquidity_plenty_dollar("QUIPU", price_plenty_dollar)
    plenty_tzbtc = await liquidity_plenty_dollar("tzBTC", price_plenty_dollar)
    plenty_wrap = await liquidity_plenty_dollar("WRAP", price_plenty_dollar)
    plenty_uno = await liquidity_plenty_dollar("UNO", price_plenty_dollar)
    plenty_kalam = await liquidity_plenty_dollar("wWBTC", price_plenty_dollar)
    plenty_smak = await liquidity_plenty_dollar("SMAK", price_plenty_dollar)
    plenty_uusd = await liquidity_plenty_dollar("uUSD", price_plenty_dollar)
    plenty_wusdt = await liquidity_plenty_dollar("wUSDT", price_plenty_dollar)
    plenty_wdai = await liquidity_plenty_dollar("wDAI", price_plenty_dollar)
    plenty_you = await liquidity_plenty_dollar("YOU", price_plenty_dollar)

    total_liquidity_plenty_dollar = \
        plenty_ctez + \
        plenty_wbusd + \
        plenty_wusdc + \
        plenty_wwbtc + \
        plenty_wmatic + \
        plenty_wlink + \
        plenty_usdtz + \
        plenty_hdao + \
        plenty_wweth + \
        plenty_kusd + \
        plenty_quipu + \
        plenty_tzbtc + \
        plenty_wrap + \
        plenty_uno + \
        plenty_kalam + \
        plenty_smak + \
        plenty_uusd + \
        plenty_wusdt + \
        plenty_wdai + \
        plenty_you

    liquidity_change_plenty = await plenty_liquidity_change_percentage_days(total_liquidity_plenty_dollar, 7)

    plentyStats = models.PlentyStats(
        symbol_plenty=symbol_plenty,
        price=price_plenty_dollar,
        price_change_percentage=price_change_plenty,
        volume_token=volume_plenty_dollar,
        volume_change_percentage=volume_change_plenty,
        liquidity=total_liquidity_plenty_dollar,
        liquidity_change=liquidity_change_plenty,
        level=level_block,
        timestamp=timestamp_now,
    )
    await plentyStats.save()
