from pydantic import BaseModel
from datetime import datetime
from typing import Optional

class OrdenRead(BaseModel):
    ordenid: int
    clienteid: int
    fechaorden: datetime
    totalprendas: int
    estado: str
    pago: int
    

    class Config:
        from_attributes = True

class OrdenCreate(BaseModel):
    clienteid: int
    fechaorden: datetime
    totalprendas: int
    estado: str
    pago: int


class OrdenUpdate(BaseModel):
    clienteid: Optional[int] = None
    fechaorden: Optional[datetime] = None
    totalprendas: Optional[int] = None
    estado: Optional[str] = None
    pago: Optional[int] = None
