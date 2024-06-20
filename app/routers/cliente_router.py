from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session
from sqlalchemy.exc import SQLAlchemyError
from ..db.database import get_db
from ..models.cliente import Cliente
from ..models.orden import Orden
from ..schemas.cliente_schema import ClienteCreate, ClienteRead

router = APIRouter()

@router.post("/clientes/", response_model=ClienteRead)
async def create_cliente(cliente: ClienteCreate, db: Session = Depends(get_db)):
    try:
        db_cliente = Cliente(nombre=cliente.nombre, apellido=cliente.apellido, telefono=cliente.telefono)
        db.add(db_cliente)
        db.commit()
        db.refresh(db_cliente)
        return db_cliente
    except SQLAlchemyError as e:
        db.rollback()
        raise HTTPException(status_code=500, detail="Error creating client") from e

@router.get("/clientes/", response_model=ClienteRead)
async def read_clientes(cliente_nombre: str, estado = 'Recibido', db: Session = Depends(get_db)):
    try:
        cliente = db.query(Cliente).filter(Cliente.nombre == cliente_nombre).first()
        if not cliente:
            raise HTTPException(status_code=404, detail="Cliente not found")
        cliente.ordenes = db.query(Orden).filter(Orden.clienteid == cliente.clienteid, Orden.estado == estado).all()
        return cliente
    except SQLAlchemyError as e:
        raise HTTPException(status_code=500, detail="Error reading clients") from e

@router.delete("/cliente/{clienteid}", response_model=ClienteRead)
async def delete_orden(clienteid: int, db: Session = Depends(get_db)):
    try:
        db_cliente = db.query(Cliente).filter(Cliente.clienteid == clienteid).first()
        if db_cliente is None:
            raise HTTPException(status_code=404, detail="Cliente no encontrado")
        
        db.delete(db_cliente)
        db.commit()
        return db_cliente
    except SQLAlchemyError as e:
        db.rollback()
        raise HTTPException(status_code=400, detail=f"Error al eliminar el cliente: {str(e)}")
    


    