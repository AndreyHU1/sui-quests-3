from enum import Enum
from typing import Optional

from pydantic import BaseModel
from pysui import SuiConfig
from pysui.sui.sui_txn import SyncTransaction
from pysui.sui.sui_types.scalars import ObjectID


class Arrow(Enum):
    RIGHT = 0
    DOWN = 1
    UP = 2
    LEFT = 3


class CoinflipSide(Enum):
    TAILS = 0
    HEADS = 1


class SuiletteColor(Enum):
    RED = 0
    BLACK = 1


class Sui8192TransactionResult(BaseModel):
    address: str
    digest: str


class Sui8192MoveResult(Sui8192TransactionResult):
    move: Arrow
    reason: Optional[str]


class SuiTxResult(Sui8192TransactionResult):
    reason: Optional[str]


class SuiBalance(BaseModel):
    int: int
    float: float


class SuiTransferConfig(BaseModel):
    config: SuiConfig
    address: str

    class Config:
        arbitrary_types_allowed = True


class SuiTx(BaseModel):
    builder: SyncTransaction
    gas: ObjectID
    merge_count: Optional[int]

    class Config:
        arbitrary_types_allowed = True
