from pydantic import BaseModel
from typing import Optional


class MagicItemBase(BaseModel):
    name: str
    description: Optional[str]
    level: Optional[int]
    type: Optional[str]
    category: Optional[str]
    weight: Optional[float]
    durability: Optional[float]
    value: Optional[int]


class MagicItemCreate(MagicItemBase):
    pass


class MagicItemRead(MagicItemBase):
    id: int
    rarity_value: float
    rarity_category: str

    class Config:
        orm_mode = True


class CreateItemRequest(BaseModel):
    name: str
    description: str = None
    level: int = None
    type: str = None
    category: str = None
    value: int = None
