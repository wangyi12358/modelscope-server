from typing import List
from pydantic import BaseModel


class FaqSupportReq(BaseModel):
    label: str
    answer: str
    text: str


class FaqReq(BaseModel):
    inputContent: List[str]
    supports: List[FaqSupportReq]
