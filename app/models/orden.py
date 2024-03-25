from sqlalchemy import Column, Integer, String, DateTime
from sqlalchemy.orm import declarative_base

Base = declarative_base()

class Orden(Base):
    __tablename__ = 'orden'  # Nombre de la tabla en tu base de datos
    
    ordenid = Column(Integer, primary_key=True, index=True)
    clienteid = Column(Integer, index=True)
    fechaorden = Column(DateTime, index=True)
    totalprendas = Column(Integer, index=True)
    estado = Column(String, index=True)
    pago = Column(Integer, index=True)

    def __repr__(self):
        return f"<Orden(ordenid={self.ordenid}, clienteid={self.clienteid}, fechaorden={self.fechaorden}, totalprendas={self.totalprendas}, estado={self.estado}, pago={self.pago})>"
