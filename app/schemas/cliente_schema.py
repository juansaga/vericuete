from pydantic import BaseModel
from datetime import datetime
from typing import List
from .orden_schema import OrdenRead

class ClienteRead(BaseModel):
    clienteid: int
    nombre: str
    apellido: str
    telefono: int
    ordenes: List[OrdenRead] = []
    class Config:
        from_attributes = True

class ClienteCreate(BaseModel):
    nombre: str
    apellido: str
    telefono: int
