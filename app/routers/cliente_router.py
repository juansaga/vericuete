from fastapi import APIRouter, HTTPException, Depends
from typing import List
from sqlalchemy.orm import Session
from ..db.database import get_db
from ..models.cliente import Cliente
from ..schemas.cliente_schema import ClienteCreate, ClienteRead

router = APIRouter()

@router.post("/clientes/", response_model=ClienteRead)
async def create_cliente(cliente: ClienteCreate, db: Session = Depends(get_db)):
    db_cliente = Cliente(nombre=cliente.nombre, apellido=cliente.apellido, telefono=cliente.telefono)
    db.add(db_cliente)
    db.commit()
    db.refresh(db_cliente)
    return db_cliente

@router.get("/clientes/", response_model=List[ClienteRead])
async def read_clientes(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    clientes = db.query(Cliente).offset(skip).limit(limit).all()
    return clientes