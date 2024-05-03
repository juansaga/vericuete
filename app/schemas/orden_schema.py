from pydantic import BaseModel
from datetime import datetime

class OrdenRead(BaseModel):
    ordenid: int
    clienteid: int
    fechaorden: datetime
    totalprendas: int
    estado: str
    pago: int
    

    class Config:
        orm_mode = True

class OrdenCreate(BaseModel):
    clienteid: int
    fechaorden: datetime
    totalprendas: int
    estado: str
    pago: int
