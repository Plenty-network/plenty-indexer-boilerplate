from decimal import Decimal
import plenty.models as models

from dipdup.context import HandlerContext
from dipdup.models import Origination
from plenty.types.plenty_fa12_fa12.storage import PlentyFa12Fa12Storage


async def on_fa12_fa12_origination(
        ctx: HandlerContext,
        plenty_fa12_fa12_origination: Origination[PlentyFa12Fa12Storage],
) -> None:
    ...
