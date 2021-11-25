from decimal import Decimal
import plenty.models as models

from plenty.types.lp_fa12.storage import LpFa12Storage
from plenty.types.plenty_fa12_fa12.parameter.remove_liquidity import RemoveLiquidityParameter
from plenty.types.lp_fa12.parameter.burn import BurnParameter
from dipdup.models import Transaction
from plenty.types.fa12_token.parameter.transfer import TransferParameter
from dipdup.context import HandlerContext
from plenty.types.fa12_token.storage import Fa12TokenStorage
from plenty.types.plenty_fa12_fa12.storage import PlentyFa12Fa12Storage


async def on_fa12_and_fa12_remove_liquidity(
        ctx: HandlerContext,
        remove_liquidity: Transaction[RemoveLiquidityParameter, PlentyFa12Fa12Storage],
        burn: Transaction[BurnParameter, LpFa12Storage],
        transfer_0: Transaction[TransferParameter, Fa12TokenStorage],
        transfer_1: Transaction[TransferParameter, Fa12TokenStorage],
) -> None:
    # SET VALUES FOR MODEL
    decimals_1 = int(ctx.template_values['decimals_1'])
    decimals_2 = int(ctx.template_values['decimals_2'])
    decimals_lp = int(ctx.template_values['decimals_lp'])
    symbol_1 = ctx.template_values['symbol_1']
    symbol_2 = ctx.template_values['symbol_2']
    symbol_lp = ctx.template_values['symbol_lp']
    trader = remove_liquidity.data.sender_address
    lp_fee = Decimal(remove_liquidity.storage.lpFee)

    # SET TOKEN QUANTITIES
    token1_quantity = Decimal(transfer_0.parameter.value) / (10 ** decimals_1)
    token2_quantity = Decimal(transfer_1.parameter.value) / (10 ** decimals_2)
    burn_quantity = Decimal(burn.parameter.value) / (10 ** decimals_lp)

    # SET POOL QUANTITIES FOR CALCULATING PRICE
    token1_pool = Decimal(remove_liquidity.storage.token1_pool) / (10 ** decimals_1)
    token2_pool = Decimal(remove_liquidity.storage.token2_pool) / (10 ** decimals_2)
    price = Decimal(token1_pool / token2_pool)


    # SAVE MODEL TO DB
    position = models.Position(
        symbol_1=symbol_1,
        symbol_2=symbol_2,
        symbol_lp=symbol_lp,
        trader=trader,
        side_liquidity=models.LiquiditySide.REMOVE,
        quantity_tk1=token1_quantity,
        quantity_tk2=token2_quantity,
        quantity_mint=0,
        quantity_burn=burn_quantity,
        quantity_pool1=token1_pool,
        quantity_pool2=token2_pool,
        price=price,
        lp_fee=lp_fee,
        level=transfer_0.data.level,
        timestamp=transfer_1.data.timestamp
    )
    await position.save()

