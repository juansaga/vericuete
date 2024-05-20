from pydantic import BaseModel

class ClienteRead(BaseModel):
    clienteid: int
    nombre: str
    apellido: str
    telefono: str

    class Config:
        orm_mode = True

class ClienteCreate(BaseModel):
    nombre: str
    apellido: str
    telefono: str
