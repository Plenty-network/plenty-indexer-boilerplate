from decimal import Decimal
import plenty.models as models

from plenty.types.fa1_token.parameter.transfer import TransferParameter as TransferParameter2
from plenty.types.lp_fa12.storage import LpFa12Storage
from dipdup.models import Transaction
from plenty.types.fa12_token.parameter.transfer import TransferParameter as TransferParameter1
from plenty.types.lp_fa12.parameter.mint import MintParameter
from dipdup.context import HandlerContext
from plenty.types.fa12_token.storage import Fa12TokenStorage
from plenty.types.plenty_fa1_fa12.storage import PlentyFa1Fa12Storage
from plenty.types.fa1_token.storage import Fa1TokenStorage
from plenty.types.plenty_fa1_fa12.parameter.add_liquidity import AddLiquidityParameter


async def on_fa1_and_fa12_add_liquidity(
        ctx: HandlerContext,
        add_liquidity: Transaction[AddLiquidityParameter, PlentyFa1Fa12Storage],
        transfer_0: Transaction[TransferParameter1, Fa12TokenStorage],
        transfer_1: Transaction[TransferParameter2, Fa1TokenStorage],
        mint: Transaction[MintParameter, LpFa12Storage],
) -> None:
    # SET VALUES FOR MODEL POSITION
    decimals_1 = int(ctx.template_values['decimals_1'])
    decimals_2 = int(ctx.template_values['decimals_2'])
    decimals_lp = int(ctx.template_values['decimals_lp'])
    symbol_1 = ctx.template_values['symbol_1']
    symbol_2 = ctx.template_values['symbol_2']
    symbol_lp = ctx.template_values['symbol_lp']
    trader = add_liquidity.data.sender_address
    lp_fee = Decimal(add_liquidity.storage.lpFee)

    # SET TOKEN QUANTITIES FOR MODEL
    token1_quantity = Decimal(transfer_0.parameter.value) / (10 ** decimals_1)
    token2_quantity = Decimal(transfer_1.parameter.value) / (10 ** decimals_2)
    mint_quantity = Decimal(mint.parameter.value) / (10 ** decimals_lp)

    # CALCULATING LP PRICE
    token1_pool = Decimal(add_liquidity.storage.token1_pool) / (10 ** decimals_1)
    token2_pool = Decimal(add_liquidity.storage.token2_pool) / (10 ** decimals_2)
    price = Decimal(token1_pool / token2_pool)
    # value = token2_quantity + price * token1_quantity

    # SAVE MODEL TO DB
    position = models.Position(
        symbol_1=symbol_1,
        symbol_2=symbol_2,
        symbol_lp=symbol_lp,
        trader=trader,
        side_liquidity=models.LiquiditySide.ADD,
        quantity_tk1=token1_quantity,
        quantity_tk2=token2_quantity,
        quantity_mint=mint_quantity,
        quantity_burn=0,
        quantity_pool1=token1_pool,
        quantity_pool2=token2_pool,
        price=price,
        lp_fee=lp_fee,
        level=transfer_0.data.level,
        timestamp=transfer_1.data.timestamp
    )
    await position.save()
