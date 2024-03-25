from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import declarative_base

Base = declarative_base()

class Cliente(Base):
    __tablename__ = 'cliente'  # Nombre de la tabla en tu base de datos
    
    clienteid = Column(Integer, primary_key=True, index=True)
    nombre = Column(String, index=True)
    apellido = Column(String, index=True)
    telefono = Column(Integer, index=True)

    def __repr__(self):
        return f"<Cliente(clienteid={self.clienteid}, nombre={self.nombre}, apellido={self.apellido}, telefono={self.telefono})>"
