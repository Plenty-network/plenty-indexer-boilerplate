from decimal import Decimal
import plenty.models as models

from plenty.types.plenty_fa2_fa2.parameter.swap import SwapParameter
from plenty.types.fa2_token.parameter.transfer import TransferParameter
from plenty.types.plenty_fa2_fa2.storage import PlentyFa2Fa2Storage
from plenty.types.fa2_token.storage import Fa2TokenStorage
from dipdup.context import HandlerContext
from dipdup.models import Transaction

async def on_fa2_token2_to_fa2_token1(
    ctx: HandlerContext,
    swap: Transaction[SwapParameter, PlentyFa2Fa2Storage],
    transfer_0: Transaction[TransferParameter, Fa2TokenStorage],
    transfer_1: Transaction[TransferParameter, Fa2TokenStorage],
) -> None:
    # SET VALUES FOR MODEL
    decimals_1 = int(ctx.template_values['decimals_1'])
    symbol_1 = ctx.template_values['symbol_1']
    decimals_2 = int(ctx.template_values['decimals_2'])
    symbol_2 = ctx.template_values['symbol_2']
    trader = swap.data.sender_address
    lp_fee = Decimal(swap.storage.lpFee)

    # TODO: implemnt this code also for liquidity
    token1_id = "0"

    token1_quantity = Decimal('0.0')
    token2_quantity = Decimal('0.0')

    for index, tx in enumerate(transfer_1.parameter.__root__[0].txs):
        token_1_id = tx.token_id
        if token1_id == token_1_id:
            tx_token1_quantity = Decimal(tx.amount) / (10 ** decimals_1)
            tx_token2_quantity = Decimal(transfer_0.parameter.__root__[0].txs[index].amount) / (10 ** decimals_2)

            token1_quantity += tx_token1_quantity
            token2_quantity += tx_token2_quantity

    if token1_quantity.compare(Decimal('0.0')) == 0:
        return

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