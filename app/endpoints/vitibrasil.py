from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from typing import List
from app import crud, schemas, dependencies

router = APIRouter()

@router.get("/producao/", response_model=List[schemas.Producao])
def read_producao(skip: int = 0, limit: int = 100, db: Session = Depends(dependencies.get_db)):
    producao = crud.get_producao(db, skip=skip, limit=limit)
    return producao

@router.get("/processa_viniferas/", response_model=List[schemas.ProcessaViniferas])
def read_processa_viniferas(skip: int = 0, limit: int = 100, db: Session = Depends(dependencies.get_db)):
    processa_viniferas = crud.get_processa_viniferas(db, skip=skip, limit=limit)
    return processa_viniferas