from pydantic import BaseModel
from datetime import datetime

# Modelo para leer datos del cliente
class OrdenRead(BaseModel):
    ordenid: int
    clienteid: int
    fechaorden: datetime
    totalprendas: int
    estado: str
    pago: int
    

    class Config:
        orm_mode = True

# Modelo para crear un nuevo cliente
class OrdenCreate(BaseModel):
    clienteid: int
    fechaorden: datetime
    totalprendas: int
    estado: str
    pago: int
