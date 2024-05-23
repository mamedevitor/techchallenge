from fastapi import FastAPI
from app.endpoints import vitibrasil
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()


app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(vitibrasil.router)

@app.get("/")
def read_root():
    return {"message": "Bem-vindo à API VitiBrasil"}
