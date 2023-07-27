from typing import List

from pydantic import BaseModel


class BookBase(BaseModel):
    title: str
    authors: List[str]
