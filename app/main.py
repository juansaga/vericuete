from fastapi import FastAPI
from .routers import cliente_router, orden_router
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from .db.database import engine
from .models import cliente, orden  # Importamos los modelos para que se registren

app = FastAPI()

app.mount("/home", StaticFiles(directory="front", html=True), name="static")

# Crear las tablas en la base de datos si no existen
cliente.Base.metadata.create_all(bind=engine)
orden.Base.metadata.create_all(bind=engine)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Permite todas las origins
    allow_credentials=True,
    allow_methods=["*"],  # Permite todos los métodos
    allow_headers=["*"],  # Permite todos los headers
)

app.include_router(cliente_router.router)
app.include_router(orden_router.router)