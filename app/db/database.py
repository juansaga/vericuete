from databases import Database
from sqlalchemy import create_engine, MetaData
from sqlalchemy.orm import sessionmaker
import os

# URL de conexión a la base de datos SQLite
DATABASE_URL = "sqlite:///./sastreria.db"

# Crear el motor de la base de datos utilizando SQLAlchemy
engine = create_engine(DATABASE_URL, connect_args={"check_same_thread": False})

# Metadatos de SQLAlchemy para la recopilación de modelos
metadata = MetaData()

# Crear una instancia de Database de 'databases' para interacciones asincrónicas
database = Database(DATABASE_URL)

# Configurar una sesión de SQLAlchemy para operaciones ORM
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Función para obtener una sesión de base de datos, útil para dependencias
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
