from fastapi import APIRouter, HTTPException, Depends
from typing import List
from sqlalchemy.orm import Session
from ..db.database import get_db
from ..models.orden import Orden
from ..schemas.orden_schema import OrdenCreate, OrdenRead, OrdenUpdate
from sqlalchemy.exc import SQLAlchemyError

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
async def read_orden(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    # Realizar una consulta para obtener clientes, con soporte para paginación usando 'skip' y 'limit'
    ordenes = db.query(Orden).offset(skip).limit(limit).all()
    return ordenes

@router.put("/orden/{ordenid}", response_model=OrdenRead)
async def update_orden(ordenid: int, orden: OrdenUpdate, db: Session = Depends(get_db)):
    try:
        db_orden = db.query(Orden).filter(Orden.ordenid == ordenid).first()
        if db_orden is None:
            raise HTTPException(status_code=404, detail="Orden no encontrada")

        for key, value in orden.model_dump(exclude_unset=True).items():
            setattr(db_orden, key, value)

        db.commit()
        db.refresh(db_orden)
        return db_orden
    except SQLAlchemyError as e:
        db.rollback()
        raise HTTPException(status_code=400, detail=f"Error al actualizar la orden: {str(e)}")
    
@router.delete("/orden/{ordenid}", response_model=OrdenRead)
async def delete_orden(ordenid: int, db: Session = Depends(get_db)):
    try:
        db_orden = db.query(Orden).filter(Orden.ordenid == ordenid).first()
        if db_orden is None:
            raise HTTPException(status_code=404, detail="Orden no encontrada")
        
        db.delete(db_orden)
        db.commit()
        return db_orden
    except SQLAlchemyError as e:
        db.rollback()
        raise HTTPException(status_code=400, detail=f"Error al eliminar la orden: {str(e)}")