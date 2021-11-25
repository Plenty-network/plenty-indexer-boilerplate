from dipdup.context import HandlerContext
from dipdup.models import Origination
from plenty.types.plenty_fa1_fa12.storage import PlentyFa1Fa12Storage


async def on_fa1_fa12_origination(
        ctx: HandlerContext,
        plenty_fa1_fa12_origination: Origination[PlentyFa1Fa12Storage],
) -> None:
    ...
