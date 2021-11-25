from dipdup.context import HandlerContext
from dipdup.models import Origination
from plenty.types.plenty_fa2_fa12.storage import PlentyFa2Fa12Storage


async def on_fa2_fa12_origination(
        ctx: HandlerContext,
        plenty_fa2_fa12_origination: Origination[PlentyFa2Fa12Storage],
) -> None:
    ...
