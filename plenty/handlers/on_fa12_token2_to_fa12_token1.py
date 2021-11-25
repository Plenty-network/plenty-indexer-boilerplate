from decimal import Decimal
import plenty.models as models

from dipdup.models import Transaction
from plenty.types.fa12_token.parameter.transfer import TransferParameter
from dipdup.context import HandlerContext
from plenty.types.fa12_token.storage import Fa12TokenStorage
from plenty.types.plenty_fa12_fa12.storage import PlentyFa12Fa12Storage
from plenty.types.plenty_fa12_fa12.parameter.swap import SwapParameter


async def on_fa12_token2_to_fa12_token1(
        ctx: HandlerContext,
        swap: Transaction[SwapParameter, PlentyFa12Fa12Storage],
        transfer_0: Transaction[TransferParameter, Fa12TokenStorage],
        transfer_1: Transaction[TransferParameter, Fa12TokenStorage],
) -> None:
    # SET VALUES FOR MODEL
    decimals_1 = int(ctx.template_values['decimals_1'])
    symbol_1 = ctx.template_values['symbol_1']
    decimals_2 = int(ctx.template_values['decimals_2'])
    symbol_2 = ctx.template_values['symbol_2']
    trader = swap.data.sender_address
    lp_fee = Decimal(swap.storage.lpFee)

    # SET TOKEN QUANTITIES FOR CALCULATING PRICE AND LATER FOR CALCULATING VOLUME IN HOOKS
    token1_quantity = Decimal(transfer_1.parameter.value) / (10 ** decimals_1)
    token2_quantity = Decimal(transfer_0.parameter.value) / (10 ** decimals_2)

    # SAVE MODEL TO DB
    trade = models.Trade(
        symbol_1=symbol_1,
        symbol_2=symbol_2,
        trader=trader,
        side_trade=models.TradeSide.SELL,
        quantity_tk1=token1_quantity,
        quantity_tk2=token2_quantity,
        price=token2_quantity / token1_quantity,
        lp_fee=lp_fee,
        level=transfer_1.data.level,
        timestamp=transfer_1.data.timestamp,
    )
    await trade.save()

