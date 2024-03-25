from pydantic import BaseModel

# Modelo para leer datos del cliente
class ClienteRead(BaseModel):
    clienteid: int
    nombre: str
    apellido: str
    telefono: str

    class Config:
        orm_mode = True

# Modelo para crear un nuevo cliente
class ClienteCreate(BaseModel):
    nombre: str
    apellido: str
    telefono: str
