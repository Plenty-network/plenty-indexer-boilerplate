from datetime import datetime
from dipdup.context import HookContext

import plenty.models as models

from plenty.functions.block_level import block_level
from plenty.functions.token_stats.liquidity_token.liquidity_token1_dollar import liquidity_token1_dollar
from plenty.functions.token_stats.liquidity_token.liquidtiy_token2_dollar import liquidtiy_token2_dollar
from plenty.functions.token_stats.liquidity_token.token_liquidity_change_percentage_days import token_liquidity_change_percentage_days
from plenty.functions.token_stats.price_token.token_price_change_percentage_hours import token_price_change_percentage_hours
from plenty.functions.token_stats.price_token.token_price_dollar import token_price_dollar
from plenty.functions.token_stats.price_token.token_price_dollar_without_plenty import token_price_dollar_without_plenty
from plenty.functions.token_stats.volume_token.token_volume_change_percentage_hours import token_volume_change_percentage_hours
from plenty.functions.token_stats.volume_token.volume_token1_dollar_24hours import volume_token1_dollar_24hours
from plenty.functions.token_stats.volume_token.volume_token2_dollar_24hours import volume_token2_dollar_24hours


async def calculate_token_stats(
        ctx: HookContext,
        major: bool,
) -> None:
    # SET TIMESTAMP
    timestamp_now = datetime.utcnow()
    symbol_plenty = "PLENTY"

    # SET BLOCK LEVEL
    level_block = await block_level("PLENTY")

    # UDEFI STATS
    symbol_udefi = "uDEFI"

    price_udefi_dollar = await token_price_dollar_without_plenty("uUSD", symbol_udefi)
    price_change_udefi = await token_price_change_percentage_hours(symbol_udefi, price_udefi_dollar, 24)

    volume_udefi_dollar = await volume_token2_dollar_24hours("uUSD", symbol_udefi)
    volume_change_udefi = await token_volume_change_percentage_hours(symbol_udefi, volume_udefi_dollar, 24)

    liquidity_udefi_dollar = await liquidtiy_token2_dollar("uUSD", symbol_udefi)
    liquidity_change_udefi = await token_liquidity_change_percentage_days(symbol_udefi, liquidity_udefi_dollar, 7)

    udefiStats = models.TokenStats(
        symbol_token=symbol_udefi,
        token_price=price_udefi_dollar,
        price_change_percentage=price_change_udefi,
        volume_token=volume_udefi_dollar,
        volume_change_percentage=volume_change_udefi,
        liquidity=liquidity_udefi_dollar,
        liquidity_change=liquidity_change_udefi,
        level=level_block,
        timestamp=timestamp_now,
    )
    await udefiStats.save()

    # CTEZ STATS
    symbol_ctez = "ctez"

    price_ctez_dollar = await token_price_dollar(symbol_plenty, symbol_ctez)
    price_change_ctez = await token_price_change_percentage_hours(symbol_ctez, price_ctez_dollar, 24)

    volume_ctez_dollar = await volume_token2_dollar_24hours(symbol_plenty, symbol_ctez)
    volume_change_ctez = await token_volume_change_percentage_hours(symbol_ctez, volume_ctez_dollar, 24)

    liquidity_ctez_dollar = await liquidtiy_token2_dollar(symbol_plenty, symbol_ctez)
    liquidity_change_ctez = await token_liquidity_change_percentage_days(symbol_ctez, liquidity_ctez_dollar, 7)

    ctezStats = models.TokenStats(
        symbol_token=symbol_ctez,
        token_price=price_ctez_dollar,
        price_change_percentage=price_change_ctez,
        volume_token=volume_ctez_dollar,
        volume_change_percentage=volume_change_ctez,
        liquidity=liquidity_ctez_dollar,
        liquidity_change=liquidity_change_ctez,
        level=level_block,
        timestamp=timestamp_now,
    )
    await ctezStats.save()

    # HDAO STATS
    symbol_hdao = "hDAO"

    price_hdao_dollar = await token_price_dollar(symbol_plenty, symbol_hdao)
    price_change_hdao = await token_price_change_percentage_hours(symbol_hdao, price_hdao_dollar, 24)

    volume_hdao_dollar = await volume_token2_dollar_24hours(symbol_plenty, symbol_hdao)
    volume_change_hdao = await token_volume_change_percentage_hours(symbol_hdao, volume_hdao_dollar, 24)

    liquidity_hdao_dollar = await liquidtiy_token2_dollar(symbol_plenty, symbol_hdao)
    liquidity_change_hdao = await token_liquidity_change_percentage_days(symbol_hdao, liquidity_hdao_dollar, 7)

    hdaoStats = models.TokenStats(
        symbol_token=symbol_hdao,
        token_price=price_hdao_dollar,
        price_change_percentage=price_change_hdao,
        volume_token=volume_hdao_dollar,
        volume_change_percentage=volume_change_hdao,
        liquidity=liquidity_hdao_dollar,
        liquidity_change=liquidity_change_hdao,
        level=level_block,
        timestamp=timestamp_now,
    )
    await hdaoStats.save()

    # USDTZ STATS
    symbol_usdtz = "USDtz"

    price_usdtz_dollar = await token_price_dollar(symbol_plenty, symbol_usdtz)
    price_change_usdtz = await token_price_change_percentage_hours(symbol_usdtz, price_usdtz_dollar, 24)

    volume_plenty_usdtz = await volume_token2_dollar_24hours(symbol_plenty, symbol_usdtz)
    volume_kusd_usdtz = await volume_token2_dollar_24hours("kUSD", symbol_usdtz)
    volume_wusdc_usdtz = await volume_token2_dollar_24hours("wUSDC", symbol_usdtz)
    volume_usdtz_dollar = volume_plenty_usdtz + volume_kusd_usdtz + volume_wusdc_usdtz
    volume_change_usdtz = await token_volume_change_percentage_hours(symbol_usdtz, volume_usdtz_dollar, 24)

    liquidity_plenty_usdtz = await liquidtiy_token2_dollar(symbol_plenty, symbol_usdtz)
    liquidity_kusd_usdtz = await liquidtiy_token2_dollar("kUSD", symbol_usdtz)
    liquidity_wusdc_usdtz = await liquidtiy_token2_dollar("wUSDC", symbol_usdtz)
    liquidity_usdtz_dollar = liquidity_plenty_usdtz + liquidity_kusd_usdtz + liquidity_wusdc_usdtz
    liquidity_change_usdtz = await token_liquidity_change_percentage_days(symbol_usdtz, liquidity_usdtz_dollar, 7)

    usdtzStats = models.TokenStats(
        symbol_token=symbol_usdtz,
        token_price=price_usdtz_dollar,
        price_change_percentage=price_change_usdtz,
        volume_token=volume_usdtz_dollar,
        volume_change_percentage=volume_change_usdtz,
        liquidity=liquidity_usdtz_dollar,
        liquidity_change=liquidity_change_usdtz,
        level=level_block,
        timestamp=timestamp_now,
    )
    await usdtzStats.save()

    # ETHTZ STATS
    symbol_ethtz = "ETHtz"

    price_ethtz_dollar = await token_price_dollar(symbol_plenty, symbol_ethtz)
    price_change_ethtz = await token_price_change_percentage_hours(symbol_ethtz, price_ethtz_dollar, 24)

    volume_plenty_ethtz = await volume_token2_dollar_24hours(symbol_plenty, symbol_ethtz)
    volume_wweth_ethtz = await volume_token2_dollar_24hours("wWETH", symbol_ethtz)
    volume_ethtz_dollar = volume_plenty_ethtz + volume_wweth_ethtz

    volume_change_ethtz = await token_volume_change_percentage_hours(symbol_ethtz, volume_ethtz_dollar, 24)

    liquidity_plenty_ethtz = await liquidtiy_token2_dollar(symbol_plenty, symbol_ethtz)
    liquidity_wweth_ethtz = await liquidtiy_token2_dollar("wWETH", symbol_ethtz)
    liquidity_ethtz_dollar = liquidity_plenty_ethtz + liquidity_wweth_ethtz
    liquidity_change_ethtz = await token_liquidity_change_percentage_days(symbol_ethtz, liquidity_ethtz_dollar, 7)

    ethtzStats = models.TokenStats(
        symbol_token=symbol_ethtz,
        token_price=price_ethtz_dollar,
        price_change_percentage=price_change_ethtz,
        volume_token=volume_ethtz_dollar,
        volume_change_percentage=volume_change_ethtz,
        liquidity=liquidity_ethtz_dollar,
        liquidity_change=liquidity_change_ethtz,
        level=level_block,
        timestamp=timestamp_now,
    )
    await ethtzStats.save()

    # GIF STATS
    symbol_gif = "GIF"

    price_gif_dollar = await token_price_dollar(symbol_plenty, symbol_gif)
    price_change_gif = await token_price_change_percentage_hours(symbol_gif, price_gif_dollar, 24)

    volume_gif_dollar = await volume_token2_dollar_24hours(symbol_plenty, symbol_gif)
    volume_change_gif = await token_volume_change_percentage_hours(symbol_gif, volume_gif_dollar, 24)

    liquidity_gif_dollar = await liquidtiy_token2_dollar(symbol_plenty, symbol_gif)
    liquidity_change_gif = await token_liquidity_change_percentage_days(symbol_gif, liquidity_gif_dollar, 7)

    gifStats = models.TokenStats(
        symbol_token=symbol_gif,
        token_price=price_gif_dollar,
        price_change_percentage=price_change_gif,
        volume_token=volume_gif_dollar,
        volume_change_percentage=volume_change_gif,
        liquidity=liquidity_gif_dollar,
        liquidity_change=liquidity_change_gif,
        level=level_block,
        timestamp=timestamp_now,
    )
    await gifStats.save()

    # SMAK STATS
    symbol_smak = "SMAK"

    price_smak_dollar = await token_price_dollar(symbol_plenty, symbol_smak)
    price_change_smak = await token_price_change_percentage_hours(symbol_smak, price_smak_dollar, 24)

    volume_smak_dollar = await volume_token2_dollar_24hours(symbol_plenty, symbol_smak)
    volume_change_smak = await token_volume_change_percentage_hours(symbol_smak, volume_smak_dollar, 24)

    liquidity_smak_dollar = await liquidtiy_token2_dollar(symbol_plenty, symbol_smak)
    liquidity_change_smak = await token_liquidity_change_percentage_days(symbol_smak, liquidity_smak_dollar, 7)

    smakStats = models.TokenStats(
        symbol_token=symbol_smak,
        token_price=price_smak_dollar,
        price_change_percentage=price_change_smak,
        volume_token=volume_smak_dollar,
        volume_change_percentage=volume_change_smak,
        liquidity=liquidity_smak_dollar,
        liquidity_change=liquidity_change_smak,
        level=level_block,
        timestamp=timestamp_now,
    )
    await smakStats.save()

    # WBUSD STATS
    symbol_wbusd = "wBUSD"

    price_wbusd_dollar = await token_price_dollar(symbol_plenty, symbol_wbusd)
    price_change_wbusd = await token_price_change_percentage_hours(symbol_wbusd, price_wbusd_dollar, 24)

    volume_wbusd_dollar = await volume_token2_dollar_24hours(symbol_plenty, symbol_wbusd)
    volume_change_wbusd = await token_volume_change_percentage_hours(symbol_wbusd, volume_wbusd_dollar, 24)

    liquidity_wbusd_dollar = await liquidtiy_token2_dollar(symbol_plenty, symbol_wbusd)
    liquidity_change_wbusd = await token_liquidity_change_percentage_days(symbol_wbusd, liquidity_wbusd_dollar, 7)

    wbusdStats = models.TokenStats(
        symbol_token=symbol_wbusd,
        token_price=price_wbusd_dollar,
        price_change_percentage=price_change_wbusd,
        volume_token=volume_wbusd_dollar,
        volume_change_percentage=volume_change_wbusd,
        liquidity=liquidity_wbusd_dollar,
        liquidity_change=liquidity_change_wbusd,
        level=level_block,
        timestamp=timestamp_now,
    )
    await wbusdStats.save()

    # WUSDC STATS
    symbol_wusdc = "wUSDC"

    price_wusdc_dollar = await token_price_dollar(symbol_plenty, symbol_wusdc)
    price_change_wusdc = await token_price_change_percentage_hours(symbol_wusdc, price_wusdc_dollar, 24)

    volume_plenty_wusdc = await volume_token2_dollar_24hours(symbol_plenty, symbol_wusdc)
    volume_wusdc_usdtz = await volume_token1_dollar_24hours(symbol_wusdc, "USDtz")
    volume_uusd_wusdc = await volume_token2_dollar_24hours("uUSD", symbol_wusdc)
    volume_wusdc_dollar = volume_plenty_wusdc + volume_wusdc_usdtz + volume_uusd_wusdc
    volume_change_wusdc = await token_volume_change_percentage_hours(symbol_wusdc, volume_wusdc_dollar, 24)

    liquidity_plenty_wusdc = await liquidtiy_token2_dollar(symbol_plenty, symbol_wusdc)
    liquidity_wusdc_usdtz = await liquidity_token1_dollar(symbol_wusdc, "USDtz")
    liquidity_uusd_wusdc = await liquidtiy_token2_dollar("uUSD", symbol_wusdc)
    liquidity_wusdc_dollar = liquidity_plenty_wusdc + liquidity_wusdc_usdtz + liquidity_uusd_wusdc
    liquidity_change_wusdc = await token_liquidity_change_percentage_days(symbol_wusdc, liquidity_wusdc_dollar, 7)

    # save model to DB
    wusdcStats = models.TokenStats(
        symbol_token=symbol_wusdc,
        token_price=price_wusdc_dollar,
        price_change_percentage=price_change_wusdc,
        volume_token=volume_wusdc_dollar,
        volume_change_percentage=volume_change_wusdc,
        liquidity=liquidity_wusdc_dollar,
        liquidity_change=liquidity_change_wusdc,
        level=level_block,
        timestamp=timestamp_now,
    )
    await wusdcStats.save()

    # WWBTC STATS
    symbol_wwbtc = "wWBTC"

    price_wwbtc_dollar = await token_price_dollar(symbol_plenty, symbol_wwbtc)
    price_change_wwbtc = await token_price_change_percentage_hours(symbol_wwbtc, price_wwbtc_dollar, 24)

    volume_wwbtc_dollar = await volume_token2_dollar_24hours(symbol_plenty, symbol_wwbtc)
    volume_change_wwbtc = await token_volume_change_percentage_hours(symbol_wwbtc, volume_wwbtc_dollar,24)

    liquidity_wwbtc_dollar = await liquidtiy_token2_dollar(symbol_plenty, symbol_wwbtc)
    liquidity_change_wwbtc = await token_liquidity_change_percentage_days(symbol_wwbtc, liquidity_wwbtc_dollar, 7)

    wwbtcStats = models.TokenStats(
        symbol_token=symbol_wwbtc,
        token_price=price_wwbtc_dollar,
        price_change_percentage=price_change_wwbtc,
        volume_token=volume_wwbtc_dollar,
        volume_change_percentage=volume_change_wwbtc,
        liquidity=liquidity_wwbtc_dollar,
        liquidity_change=liquidity_change_wwbtc,
        level=level_block,
        timestamp=timestamp_now,
    )
    await wwbtcStats.save()

    # WMATIC STATS
    symbol_wmatic = "wMATIC"

    price_wmatic_dollar = await token_price_dollar(symbol_plenty, symbol_wmatic)
    price_change_wmatic = await token_price_change_percentage_hours(symbol_wmatic, price_wmatic_dollar, 24)

    volume_wmatic_dollar = await volume_token2_dollar_24hours(symbol_plenty, symbol_wmatic)
    volume_change_wmatic = await token_volume_change_percentage_hours(symbol_wmatic, volume_wmatic_dollar, 24)

    liquidity_wmatic_dollar = await liquidtiy_token2_dollar(symbol_plenty, symbol_wmatic)
    liquidity_change_wmatic = await token_liquidity_change_percentage_days(symbol_wmatic, liquidity_wmatic_dollar, 7)

    wmaticStats = models.TokenStats(
        symbol_token=symbol_wmatic,
        token_price=price_wmatic_dollar,
        price_change_percentage=price_change_wmatic,
        volume_token=volume_wmatic_dollar,
        volume_change_percentage=volume_change_wmatic,
        liquidity=liquidity_wmatic_dollar,
        liquidity_change=liquidity_change_wmatic,
        level=level_block,
        timestamp=timestamp_now,
    )
    await wmaticStats.save()

    # WLINK STATS
    symbol_wlink = "wLINK"

    price_wlink_dollar = await token_price_dollar(symbol_plenty, symbol_wlink)
    price_change_wlink = await token_price_change_percentage_hours(symbol_wlink, price_wlink_dollar, 24)

    volume_wlink_dollar = await volume_token2_dollar_24hours(symbol_plenty, symbol_wlink)
    volume_change_wlink = await token_volume_change_percentage_hours(symbol_wlink, volume_wlink_dollar, 24)

    liquidity_wlink_dollar = await liquidtiy_token2_dollar(symbol_plenty, symbol_wlink)
    liquidity_change_wlink = await token_liquidity_change_percentage_days(symbol_wlink, liquidity_wlink_dollar, 7)

    wlinkStats = models.TokenStats(
        symbol_token=symbol_wlink,
        token_price=price_wlink_dollar,
        price_change_percentage=price_change_wlink,
        volume_token=volume_wlink_dollar,
        volume_change_percentage=volume_change_wlink,
        liquidity=liquidity_wlink_dollar,
        liquidity_change=liquidity_change_wlink,
        level=level_block,
        timestamp=timestamp_now,
    )
    await wlinkStats.save()

    # WWETH STATS
    symbol_wweth = "wWETH"

    price_wweth_dollar = await token_price_dollar(symbol_plenty, symbol_wweth)
    price_change_wweth = await token_price_change_percentage_hours(symbol_wweth, price_wweth_dollar, 24)

    volume_plenty_wweth = await volume_token2_dollar_24hours(symbol_plenty, symbol_wweth)
    volume_wweth_ethtz = await volume_token1_dollar_24hours(symbol_wweth, "ETHtz")
    volume_wweth_dollar = volume_plenty_wweth + volume_wweth_ethtz
    volume_change_wweth = await token_volume_change_percentage_hours(symbol_wweth, volume_wweth_dollar, 24)

    liquidity_plenty_wweth = await liquidtiy_token2_dollar(symbol_plenty, symbol_wweth)
    liquidity_wweth_ethtz = await liquidity_token1_dollar(symbol_wweth, "ETHtz")
    liquidity_wweth_dollar = liquidity_plenty_wweth + liquidity_wweth_ethtz
    liquidity_change_wweth = await token_liquidity_change_percentage_days(symbol_wweth, liquidity_wweth_dollar, 7)

    wwethStats = models.TokenStats(
        symbol_token=symbol_wweth,
        token_price=price_wweth_dollar,
        price_change_percentage=price_change_wweth,
        volume_token=volume_wweth_dollar,
        volume_change_percentage=volume_change_wweth,
        liquidity=liquidity_wweth_dollar,
        liquidity_change=liquidity_change_wweth,
        level=level_block,
        timestamp=timestamp_now,
    )
    await wwethStats.save()

    # KUSD STATS
    symbol_kusd = "kUSD"

    price_kusd_dollar = await token_price_dollar(symbol_plenty, symbol_kusd)
    price_change_kusd = await token_price_change_percentage_hours(symbol_kusd, price_kusd_dollar, 24)

    volume_plenty_kusd = await volume_token2_dollar_24hours(symbol_plenty, symbol_kusd)
    volume_kusd_usdtz = await volume_token1_dollar_24hours(symbol_kusd, "USDtz")
    volume_kusd_dollar = volume_plenty_kusd + volume_kusd_usdtz
    volume_change_kusd = await token_volume_change_percentage_hours(symbol_kusd, volume_kusd_dollar, 24)

    liquidity_plenty_kusd = await liquidtiy_token2_dollar(symbol_plenty, symbol_kusd)
    liquidity_kusd_usdtz = await liquidity_token1_dollar(symbol_kusd, "USDtz")
    liquidity_kusd_dollar = liquidity_plenty_kusd + liquidity_kusd_usdtz
    liquidity_change_kusd = await token_liquidity_change_percentage_days(symbol_kusd, liquidity_kusd_dollar, 7)

    kusdStats = models.TokenStats(
        symbol_token=symbol_kusd,
        token_price=price_kusd_dollar,
        price_change_percentage=price_change_kusd,
        volume_token=volume_kusd_dollar,
        volume_change_percentage=volume_change_kusd,
        liquidity=liquidity_kusd_dollar,
        liquidity_change=liquidity_change_kusd,
        level=level_block,
        timestamp=timestamp_now,
    )
    await kusdStats.save()

    # QUIPU STATS
    symbol_quipu = "QUIPU"

    price_quipu_dollar = await token_price_dollar(symbol_plenty, symbol_quipu)
    price_change_quipu = await token_price_change_percentage_hours(symbol_quipu, price_quipu_dollar, 24)

    volume_quipu_dollar = await volume_token2_dollar_24hours(symbol_plenty, symbol_quipu)
    volume_change_quipu = await token_volume_change_percentage_hours(symbol_quipu, volume_quipu_dollar, 24)

    liquidity_quipu_dollar = await liquidtiy_token2_dollar(symbol_plenty, symbol_quipu)
    liquidity_change_quipu = await token_liquidity_change_percentage_days(symbol_quipu, liquidity_quipu_dollar, 7)

    quipuStats = models.TokenStats(
        symbol_token=symbol_quipu,
        token_price=price_quipu_dollar,
        price_change_percentage=price_change_quipu,
        volume_token=volume_quipu_dollar,
        volume_change_percentage=volume_change_quipu,
        liquidity=liquidity_quipu_dollar,
        liquidity_change=liquidity_change_quipu,
        level=level_block,
        timestamp=timestamp_now,
    )
    await quipuStats.save()

    # TZBTC STATS
    symbol_tzbtc = "tzBTC"

    price_tzbtc_dollar = await token_price_dollar(symbol_plenty, symbol_tzbtc)
    price_change_tzbtc = await token_price_change_percentage_hours(symbol_tzbtc, price_tzbtc_dollar, 24)

    volume_tzbtc_dollar = await volume_token2_dollar_24hours(symbol_plenty, symbol_tzbtc)
    volume_change_tzbtc = await token_volume_change_percentage_hours(symbol_tzbtc, volume_tzbtc_dollar, 24)

    liquidity_tzbtc_dollar = await liquidtiy_token2_dollar(symbol_plenty, symbol_tzbtc)
    liquidity_change_tzbtc = await token_liquidity_change_percentage_days(symbol_tzbtc, liquidity_tzbtc_dollar, 7)

    tzbtcStats = models.TokenStats(
        symbol_token=symbol_tzbtc,
        token_price=price_tzbtc_dollar,
        price_change_percentage=price_change_tzbtc,
        volume_token=volume_tzbtc_dollar,
        volume_change_percentage=volume_change_tzbtc,
        liquidity=liquidity_tzbtc_dollar,
        liquidity_change=liquidity_change_tzbtc,
        level=level_block,
        timestamp=timestamp_now,
    )
    await tzbtcStats.save()

    # WRAP STATS
    symbol_wrap = "WRAP"

    price_wrap_dollar = await token_price_dollar(symbol_plenty, symbol_wrap)
    price_change_wrap = await token_price_change_percentage_hours(symbol_wrap, price_wrap_dollar, 24)

    volume_wrap_dollar = await volume_token2_dollar_24hours(symbol_plenty, symbol_wrap)
    volume_change_wrap = await token_volume_change_percentage_hours(symbol_wrap, volume_wrap_dollar, 24)

    liquidity_wrap_dollar = await liquidtiy_token2_dollar(symbol_plenty, symbol_wrap)
    liquidity_change_wrap = await token_liquidity_change_percentage_days(symbol_wrap, liquidity_wrap_dollar, 7)

    wrapStats = models.TokenStats(
        symbol_token=symbol_wrap,
        token_price=price_wrap_dollar,
        price_change_percentage=price_change_wrap,
        volume_token=volume_wrap_dollar,
        volume_change_percentage=volume_change_wrap,
        liquidity=liquidity_wrap_dollar,
        liquidity_change=liquidity_change_wrap,
        level=level_block,
        timestamp=timestamp_now,
    )
    await wrapStats.save()

    # UNO STATS
    symbol_uno = "UNO"

    price_uno_dollar = await token_price_dollar(symbol_plenty, symbol_uno)
    price_change_uno = await token_price_change_percentage_hours(symbol_uno, price_uno_dollar, 24)

    volume_uno_dollar = await volume_token2_dollar_24hours(symbol_plenty, symbol_uno)
    volume_change_uno = await token_volume_change_percentage_hours(symbol_uno, volume_uno_dollar, 24)

    liquidity_uno_dollar = await liquidtiy_token2_dollar(symbol_plenty, symbol_uno)
    liquidity_change_uno = await token_liquidity_change_percentage_days(symbol_uno, liquidity_uno_dollar, 7)

    unoStats = models.TokenStats(
        symbol_token=symbol_uno,
        token_price=price_uno_dollar,
        price_change_percentage=price_change_uno,
        volume_token=volume_uno_dollar,
        volume_change_percentage=volume_change_uno,
        liquidity=liquidity_uno_dollar,
        liquidity_change=liquidity_change_uno,
        level=level_block,
        timestamp=timestamp_now,
    )
    await unoStats.save()

    # KALAM STATS
    symbol_kalam = "KALAM"

    price_kalam_dollar = await token_price_dollar(symbol_plenty, symbol_kalam)
    price_change_kalam = await token_price_change_percentage_hours(symbol_kalam, price_kalam_dollar, 24)

    volume_kalam_dollar = await volume_token2_dollar_24hours(symbol_plenty, symbol_kalam)
    volume_change_kalam = await token_volume_change_percentage_hours(symbol_kalam, volume_kalam_dollar, 24)

    liquidity_kalam_dollar = await liquidtiy_token2_dollar(symbol_plenty, symbol_kalam)
    liquidity_change_kalam = await token_liquidity_change_percentage_days(symbol_kalam, liquidity_kalam_dollar, 7)

    kalamStats = models.TokenStats(
        symbol_token=symbol_kalam,
        token_price=price_kalam_dollar,
        price_change_percentage=price_change_kalam,
        volume_token=volume_kalam_dollar,
        volume_change_percentage=volume_change_kalam,
        liquidity=liquidity_kalam_dollar,
        liquidity_change=liquidity_change_kalam,
        level=level_block,
        timestamp=timestamp_now,
    )
    await kalamStats.save()

    # UUSD STATS
    symbol_uusd = "uUSD"

    price_uusd_dollar = await token_price_dollar(symbol_plenty, symbol_uusd)
    price_change_uusd = await token_price_change_percentage_hours(symbol_uusd, price_uusd_dollar, 24)

    volume_plenty_uusd = await volume_token2_dollar_24hours(symbol_plenty, symbol_uusd)
    volume_uusd_wusdc = await volume_token1_dollar_24hours(symbol_uusd, "wUSDC")
    volume_uusd_udefi = await volume_token1_dollar_24hours(symbol_uusd, "uDEFI")
    volume_uusd_you = await volume_token1_dollar_24hours(symbol_uusd, "YOU")
    volume_uusd_dollar = volume_plenty_uusd + volume_uusd_wusdc + volume_uusd_udefi + volume_uusd_you
    volume_change_uusd = await token_volume_change_percentage_hours(symbol_uusd, volume_uusd_dollar, 24)

    liquidity_plenty_uusd = await liquidtiy_token2_dollar(symbol_plenty, symbol_uusd)
    liquidity_uusd_wusdc =  await liquidity_token1_dollar(symbol_uusd, "wUSDC")
    liquidity_uusd_udefi = await liquidity_token1_dollar(symbol_uusd, "uDEFI")
    liquidity_uusd_you = await liquidity_token1_dollar(symbol_uusd, "uDEFI")
    liquidity_uusd_dollar = liquidity_plenty_uusd + liquidity_uusd_wusdc + liquidity_uusd_udefi + liquidity_uusd_you
    liquidity_change_uusd = await token_liquidity_change_percentage_days(symbol_uusd, liquidity_uusd_dollar, 7)

    uusdStats = models.TokenStats(
        symbol_token=symbol_uusd,
        token_price=price_uusd_dollar,
        price_change_percentage=price_change_uusd,
        volume_token=volume_plenty_uusd,
        volume_change_percentage=volume_change_uusd,
        liquidity=liquidity_uusd_dollar,
        liquidity_change=liquidity_change_uusd,
        level=level_block,
        timestamp=timestamp_now,
    )
    await uusdStats.save()

    # WUSDT STATS
    symbol_wusdt = "wUSDT"

    price_wusdt_dollar = await token_price_dollar(symbol_plenty, symbol_wusdt)
    price_change_wusdt = await token_price_change_percentage_hours(symbol_wusdt, price_wusdt_dollar, 24)

    volume_wusdt_dollar = await volume_token2_dollar_24hours(symbol_plenty, symbol_wusdt)
    volume_change_wusdt = await token_volume_change_percentage_hours(symbol_wusdt, volume_wusdt_dollar, 24)

    liquidity_wusdt_dollar = await liquidtiy_token2_dollar(symbol_plenty, symbol_wusdt)
    liquidity_change_wusdt = await token_liquidity_change_percentage_days(symbol_wusdt, liquidity_wusdt_dollar, 7)

    wusdtStats = models.TokenStats(
        symbol_token=symbol_wusdt,
        token_price=price_wusdt_dollar,
        price_change_percentage=price_change_wusdt,
        volume_token=volume_wusdt_dollar,
        volume_change_percentage=volume_change_wusdt,
        liquidity=liquidity_wusdt_dollar,
        liquidity_change=liquidity_change_wusdt,
        level=level_block,
        timestamp=timestamp_now,
    )
    await wusdtStats.save()

    # WDAI STATS
    symbol_wdai = "wDAI"

    price_wdai_dollar = await token_price_dollar(symbol_plenty, symbol_wdai)
    price_change_wdai = await token_price_change_percentage_hours(symbol_wdai, price_wdai_dollar, 24)

    volume_wdai_dollar = await volume_token2_dollar_24hours(symbol_plenty, symbol_wdai)
    volume_change_wdai = await token_volume_change_percentage_hours(symbol_wdai, volume_wdai_dollar, 24)

    liquidity_wdai_dollar = await liquidtiy_token2_dollar(symbol_plenty, symbol_wdai)
    liquidity_change_wdai = await token_liquidity_change_percentage_days(symbol_wdai, liquidity_wdai_dollar, 7)

    wdaiStats = models.TokenStats(
        symbol_token=symbol_wdai,
        token_price=price_wdai_dollar,
        price_change_percentage=price_change_wdai,
        volume_token=volume_wdai_dollar,
        volume_change_percentage=volume_change_wdai,
        liquidity=liquidity_wdai_dollar,
        liquidity_change=liquidity_change_wdai,
        level=level_block,
        timestamp=timestamp_now,
    )
    await wdaiStats.save()

    # YOU STATS
    symbol_you = "YOU"

    price_you_dollar = await token_price_dollar(symbol_plenty, symbol_you)
    price_change_you = await token_price_change_percentage_hours(symbol_you, price_you_dollar, 24)

    volume_you_plenty = await volume_token2_dollar_24hours(symbol_plenty, symbol_you)
    volume_uusd_you = await volume_token2_dollar_24hours("uUSD", symbol_you)
    volume_you_dollar = volume_you_plenty + volume_uusd_you
    volume_change_you = await token_volume_change_percentage_hours(symbol_you, volume_you_dollar, 24)

    liquidity_plenty_you = await liquidtiy_token2_dollar(symbol_plenty, symbol_you)
    liquidity_uusd_you = await liquidtiy_token2_dollar("uUSD", symbol_you)
    liquidity_you_dollar =liquidity_plenty_you + liquidity_uusd_you
    liquidity_change_you = await token_liquidity_change_percentage_days(symbol_you, liquidity_you_dollar, 7)

    youStats = models.TokenStats(
        symbol_token=symbol_you,
        token_price=price_you_dollar,
        price_change_percentage=price_change_you,
        volume_token=volume_you_dollar,
        volume_change_percentage=volume_change_you,
        liquidity=liquidity_you_dollar,
        liquidity_change=liquidity_change_you,
        level=level_block,
        timestamp=timestamp_now,
    )
    await youStats.save()






