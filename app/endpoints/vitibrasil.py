from fastapi import APIRouter, Depends, HTTPException
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

@router.get("/processa_uvamesa/", response_model=List[schemas.ProcessaUvaMesa])
def read_processa_uvamesa(skip: int = 0, limit: int = 100, db: Session = Depends(dependencies.get_db)):
    processa_uvamesa = crud.get_processa_uvamesa(db, skip=skip, limit=limit)
    return processa_uvamesa

@router.get("/processa_semclassf/", response_model=List[schemas.ProcessaSemClassf])
def read_processa_semclassf(skip: int = 0, limit: int = 100, db: Session = Depends(dependencies.get_db)):
    processa_semclassf = crud.get_processa_semclassf(db, skip=skip, limit=limit)
    return processa_semclassf

@router.get("/processa_americanas_hibridas/", response_model=List[schemas.ProcessaAmericanasHibridas])
def read_processa_americanas_hibridas(skip: int = 0, limit: int = 100, db: Session = Depends(dependencies.get_db)):
    processa_americanas_hibridas = crud.get_processa_americanashibridas(db, skip=skip, limit=limit)
    return processa_americanas_hibridas

@router.get("/importacao_vinhos/", response_model=List[schemas.ImportacaoVinhos])
def read_importacao_vinhos(skip: int = 0, limit: int = 100, db: Session = Depends(dependencies.get_db)):
    importacao_vinhos = crud.get_importacao_vinhos(db, skip=skip, limit=limit)
    return importacao_vinhos

@router.get("/importacao_uvaspassas/", response_model=List[schemas.ImportacaoUvasPassas])
def read_importacao_uvaspassas(skip: int = 0, limit: int = 100, db: Session = Depends(dependencies.get_db)):
    importacao_uvaspassas = crud.get_importacao_uvaspassas(db, skip=skip, limit=limit)
    return importacao_uvaspassas

@router.get("/importacao_uvasfrescas/", response_model=List[schemas.ImportacaoUvasFrescas])
def read_importacao_uvasfrescas(skip: int = 0, limit: int = 100, db: Session = Depends(dependencies.get_db)):
    importacao_uvasfrescas = crud.get_importacao_uvasfrescas(db, skip=skip, limit=limit)
    return importacao_uvasfrescas

@router.get("/importacao_suco/", response_model=List[schemas.ImportacaoSuco])
def read_importacao_suco(skip: int = 0, limit: int = 100, db: Session = Depends(dependencies.get_db)):
    importacao_suco = crud.get_importacao_suco(db, skip=skip, limit=limit)
    return importacao_suco

@router.get("/importacao_espumantes/", response_model=List[schemas.ImportacaoEspumantes])
def read_importacao_espumantes(skip: int = 0, limit: int = 100, db: Session = Depends(dependencies.get_db)):
    importacao_espumantes = crud.get_importacao_espumantes(db, skip=skip, limit=limit)
    return importacao_espumantes

@router.get("/exportacao_vinhosmesa/", response_model=List[schemas.ExportacaoVinhoMesa])
def read_exportacao_vinhosmesa(skip: int = 0, limit: int = 100, db: Session = Depends(dependencies.get_db)):
    exportacao_vinhosmesa = crud.get_exportacao_vinhomesa(db, skip=skip, limit=limit)
    return exportacao_vinhosmesa

@router.get("/exportacao_uvasfrescas/", response_model=List[schemas.ExportacaoUvasFrescas])
def read_exportacao_uvasfrescas(skip: int = 0, limit: int = 100, db: Session = Depends(dependencies.get_db)):
    exportacao_uvasfrescas = crud.get_exportacao_uvasfrescas(db, skip=skip, limit=limit)
    return exportacao_uvasfrescas

@router.get("/exportacao_suco/", response_model=List[schemas.ExportacaoSuco])
def read_exportacao_suco(skip: int = 0, limit: int = 100, db: Session = Depends(dependencies.get_db)):
    exportacao_suco = crud.get_exportacao_suco(db, skip=skip, limit=limit)
    return exportacao_suco

@router.get("/exportacao_espumantes/", response_model=List[schemas.ExportacaoEspumantes])
def read_exportacao_espumantes(skip: int = 0, limit: int = 100, db: Session = Depends(dependencies.get_db)):
    exportacao_espumantes = crud.get_exportacao_espumantes(db, skip=skip, limit=limit)
    return exportacao_espumantes

@router.get("/comercio/", response_model=List[schemas.Comercio])
def read_comercio(skip: int = 0, limit: int = 100, db: Session = Depends(dependencies.get_db)):
    comercio = crud.get_comercio(db, skip=skip, limit=limit)
    return comercio