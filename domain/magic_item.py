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
    stock: Optional[int]


class MagicItemCreate(MagicItemBase):
    pass


class MagicItemRead(MagicItemBase):
    id: int
    rarity_value: float

    # rarity_category: str

    class Config:
        orm_mode = True


class CreateItemRequest(BaseModel):
    name: str
    description: str = None
    level: int = None
    type: str = None
    category: str = None
    value: int = None
    stock: int = 1


class MagicItemUpdate(BaseModel):
    name: Optional[str] = None
    description: Optional[str] = None
    level: Optional[int] = None
    type: Optional[str] = None
    category: Optional[str] = None
    weight: Optional[float] = None
    durability: Optional[float] = None
    value: Optional[int] = None
    stock: Optional[int] = None
