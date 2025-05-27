from pydantic import BaseModel

import datetime

import uuid

from typing import Any, Dict, List, Tuple

class Collages(BaseModel):
    id: Any
    name: str


class ReadCollages(BaseModel):
    id: Any
    name: str
    class Config:
        from_attributes = True




class PostCollages(BaseModel):
    id: int
    name: str

    class Config:
        from_attributes = True

