from pydantic import BaseModel
from typing import Optional, Dict, Any


class MagicItemBase(BaseModel):
    name: str
    description: Optional[str]
    level: Optional[int]
    type: Optional[str]
    category: Optional[str]
    weight: Optional[float]
    durability: Optional[float]
    value: Optional[int]
