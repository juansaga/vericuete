from fastapi import FastAPI, HTTPException
from databases import Database
from app.models.cliente import ClienteCreate, ClienteRead
from app.models.orden import OrdenCreate, OrdenRead
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()


app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Permite todas las origins
    allow_credentials=True,
    allow_methods=["*"],  # Permite todos los métodos
    allow_headers=["*"],  # Permite todos los headers
)







# Configura tu URL de conexión a la base de datos
DATABASE_URL = "postgresql://postgres:juanma123@localhost/postgres"
database = Database(DATABASE_URL)

@app.on_event("startup")
async def startup():
    await database.connect()

@app.on_event("shutdown")
async def shutdown():
    await database.disconnect()

@app.get("/")
async def read_root():
    return {"Hello": "World"}


# Suponiendo que ya tienes la configuración inicial aquí

@app.post("/clientes/", response_model=ClienteRead)
async def create_cliente(cliente: ClienteCreate):
    query = "INSERT INTO Cliente(nombre, apellido, telefono) VALUES (:nombre, :apellido, :telefono) RETURNING *"
    return await database.fetch_one(query, cliente.dict())

@app.get("/clientes/")
async def read_cliente():
    query = f"SELECT * FROM cliente"
    response = await database.fetch_all(query)
    return response


@app.post("/ordenes/", response_model=OrdenRead)
async def create_orden(orden: OrdenCreate):
    query = "INSERT INTO Orden(clienteid, fechaorden, totalprendas, estado, pago) VALUES (:clienteid, :fechaorden, :totalprendas, :estado, :pago) RETURNING *"
    return await database.fetch_one(query, orden.dict())

@app.get("/ordenes/")
async def read_orden():
    query = f"SELECT * FROM orden"
    response = await database.fetch_all(query)
    return response