from fastapi import FastAPI
from .routers import cliente_router, orden_router
from fastapi.middleware.cors import CORSMiddleware 
from fastapi.staticfiles import StaticFiles

app = FastAPI()

app.mount("/home", StaticFiles(directory="front", html=True), name="static")

# @app.get("/")
# async def main():
#     return {"message": "Go to /home to see the site"}

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Permite todas las origins
    allow_credentials=True,
    allow_methods=["*"],  # Permite todos los métodos
    allow_headers=["*"],  # Permite todos los headers
)



app.include_router(cliente_router.router)
app.include_router(orden_router.router)
