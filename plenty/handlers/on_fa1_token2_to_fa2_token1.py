from decimal import Decimal
import plenty.models as models

from plenty.types.fa1_token.parameter.transfer import TransferParameter as TransferParameter1
from plenty.types.plenty_fa1_fa2.storage import PlentyFa1Fa2Storage
from plenty.types.fa2_token.storage import Fa2TokenStorage
from plenty.types.plenty_fa1_fa2.parameter.swap import SwapParameter
from plenty.types.fa2_token.parameter.transfer import TransferParameter as TransferParameter2
from dipdup.models import Transaction
from dipdup.context import HandlerContext
from plenty.types.fa1_token.storage import Fa1TokenStorage


async def on_fa1_token2_to_fa2_token1(
        ctx: HandlerContext,
        swap: Transaction[SwapParameter, PlentyFa1Fa2Storage],
        transfer_0: Transaction[TransferParameter1, Fa1TokenStorage],
        transfer_1: Transaction[TransferParameter2, Fa2TokenStorage],
) -> None:
    # SET VALUES FOR MODEL TRADE
    decimals_1 = int(ctx.template_values['decimals_1'])
    decimals_2 = int(ctx.template_values['decimals_2'])
    symbol_1 = ctx.template_values['symbol_1']
    symbol_2 = ctx.template_values['symbol_2']
    trader = swap.data.sender_address
    lp_fee = Decimal(swap.storage.lpFee)

    # GET TOKEN QUANTITIES FOR CALCULATING PRICE AND LATER FOR CALCULATING VOLUME IN HOOKS
    token1_quantity = sum(Decimal(tx.amount) for tx in transfer_1.parameter.__root__[0].txs) / (10 ** decimals_1)
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
