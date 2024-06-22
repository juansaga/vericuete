from fastapi import APIRouter, HTTPException, Depends
from typing import List
from sqlalchemy.orm import Session
from ..db.database import get_db
from ..models.orden import Orden
from ..schemas.orden_schema import OrdenCreate, OrdenRead

router = APIRouter()

@router.post("/orden/", response_model=OrdenRead)
async def create_orden(orden: OrdenCreate, db: Session = Depends(get_db)):
     # Crear una instancia del modelo Cliente con los datos recibidos
    db_orden = Orden(clienteid=orden.clienteid, fechaorden=orden.fechaorden, totalprendas=orden.totalprendas, estado=orden.estado, pago=orden.pago)
    # Añadir la instancia a la sesión y cometer los cambios para insertarla en la base de datos
    db.add(db_orden)
    db.commit()
    # Refrescar la instancia para asegurar que devuelve los valores después de la inserción
    db.refresh(db_orden)
    # Devolver la instancia insertada, que será automáticamente convertida al esquema Pydantic ClienteRead
    return db_orden

@router.get("/orden/", response_model=List[OrdenRead])
async def read_orden(estado, db: Session = Depends(get_db)):
    # Realizar una consulta para obtener clientes, con soporte para paginación usando 'skip' y 'limit'
    ordenes = db.query(Orden).filter(Orden.estado == estado).all()
    return ordenes
