from enum import Enum
from pydantic import BaseModel




class SnowboardBrand(Enum):
    NITRO = "Nitro"
    SALOMAN = "Saloman"
    BURTON = "Burton"




class Snowboard(BaseModel):
    id: int
    length: int
    color: str
    has_bindings: bool
    brand: SnowboardBrand