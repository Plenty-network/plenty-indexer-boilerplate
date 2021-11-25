from dipdup.context import HandlerContext
from dipdup.models import Origination
from plenty.types.plenty_fa1_fa2.storage import PlentyFa1Fa2Storage


async def on_fa1_fa2_origination(
        ctx: HandlerContext,
        plenty_fa1_fa2_origination: Origination[PlentyFa1Fa2Storage],
) -> None:
    ...
