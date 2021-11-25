from enum import IntEnum

from tortoise import Model, fields

# MODEL TRADE SIDE: ENUM BUY OR SELL
class TradeSide(IntEnum):
    BUY = 1
    SELL = 0

# MODEL LIQUIDITY SIDE: ENUM ADD OR REMOVE
class LiquiditySide(IntEnum):
    ADD = 1
    REMOVE = 0

# MODEL TRADE ON AMM
class Trade(Model):
    id = fields.IntField(pk=True)
    symbol_1 = fields.CharField(max_length=7)
    symbol_2 = fields.CharField(max_length=7)
    trader = fields.CharField(36)
    side_trade = fields.IntEnumField(enum_type=TradeSide)
    quantity_tk1 = fields.DecimalField(decimal_places=18, max_digits=1000)
    quantity_tk2 = fields.DecimalField(decimal_places=18, max_digits=1000)
    price = fields.DecimalField(decimal_places=18, max_digits=200)
    lp_fee = fields.DecimalField(decimal_places=18, max_digits=1000)
    level = fields.BigIntField()
    timestamp = fields.DatetimeField()

# MODEL LP SIDE OF AMM
class Position(Model):
    id = fields.IntField(pk=True)
    symbol_1 = fields.CharField(max_length=7)
    symbol_2 = fields.CharField(max_length=7)
    symbol_lp = fields.CharField(max_length=7)
    trader = fields.CharField(36)
    side_liquidity = fields.IntEnumField(enum_type=LiquiditySide)
    quantity_tk1 = fields.DecimalField(decimal_places=18, max_digits=1000)
    quantity_tk2 = fields.DecimalField(decimal_places=18, max_digits=1000)
    quantity_mint = fields.DecimalField(decimal_places=18, max_digits=1000)
    quantity_burn = fields.DecimalField(decimal_places=18, max_digits=1000)
    quantity_pool1 = fields.DecimalField(decimal_places=18, max_digits=1000)
    quantity_pool2 = fields.DecimalField(decimal_places=18, max_digits=1000)
    price = fields.DecimalField(decimal_places=18, max_digits=200)
    lp_fee = fields.DecimalField(decimal_places=18, max_digits=1000)
    level = fields.BigIntField()
    timestamp = fields.DatetimeField()

# MODEL STATS PLENTY TOKEN
class PlentyStats(Model):
    id = fields.IntField(pk=True)
    symbol_plenty = fields.CharField(max_length=7)
    price = fields.DecimalField(decimal_places=18, max_digits=200)
    price_change_percentage = fields.DecimalField(decimal_places=18, max_digits=200)
    volume_token = fields.DecimalField(decimal_places=18, max_digits=200)
    volume_change_percentage = fields.DecimalField(decimal_places=18, max_digits=200)
    liquidity = fields.DecimalField(decimal_places=18, max_digits=200)
    liquidity_change = fields.DecimalField(decimal_places=18, max_digits=200)
    level = fields.BigIntField()
    timestamp = fields.DatetimeField()

# MODEL STATS OTHER TOKENS
class TokenStats(Model):
    id = fields.IntField(pk=True)
    symbol_token = fields.CharField(max_length=7)
    token_price = fields.DecimalField(decimal_places=18, max_digits=200)
    price_change_percentage = fields.DecimalField(decimal_places=18, max_digits=200)
    volume_token = fields.DecimalField(decimal_places=18, max_digits=200)
    volume_change_percentage = fields.DecimalField(decimal_places=18, max_digits=200)
    liquidity = fields.DecimalField(decimal_places=18, max_digits=200)
    liquidity_change = fields.DecimalField(decimal_places=18, max_digits=200)
    level = fields.BigIntField()
    timestamp = fields.DatetimeField()
