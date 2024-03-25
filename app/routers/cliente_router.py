from fastapi import APIRouter, HTTPException, Depends
from typing import List
from sqlalchemy.orm import Session
from ..db.database import get_db
from ..models.cliente import Cliente
from ..schemas.cliente_schema import ClienteCreate, ClienteRead

router = APIRouter()

@router.post("/clientes/", response_model=ClienteRead)
async def create_cliente(cliente: ClienteCreate, db: Session = Depends(get_db)):
     # Crear una instancia del modelo Cliente con los datos recibidos
    db_cliente = Cliente(nombre=cliente.nombre, apellido=cliente.apellido, telefono=cliente.telefono)
    # Añadir la instancia a la sesión y cometer los cambios para insertarla en la base de datos
    db.add(db_cliente)
    db.commit()
    # Refrescar la instancia para asegurar que devuelve los valores después de la inserción
    db.refresh(db_cliente)
    # Devolver la instancia insertada, que será automáticamente convertida al esquema Pydantic ClienteRead
    return db_cliente

@router.get("/clientes/", response_model=List[ClienteRead])
async def read_clientes(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    # Realizar una consulta para obtener clientes, con soporte para paginación usando 'skip' y 'limit'
    clientes = db.query(Cliente).offset(skip).limit(limit).all()
    return clientes
