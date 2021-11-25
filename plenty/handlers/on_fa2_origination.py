
from plenty.types.plenty_fa2_fa2.storage import PlentyFa2Fa2Storage
from dipdup.models import Origination
from dipdup.context import HandlerContext

async def on_fa2_origination(
    ctx: HandlerContext,
    plenty_fa2_fa2_origination: Origination[PlentyFa2Fa2Storage],
) -> None:
    ...