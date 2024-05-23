from sqlalchemy.orm import Session
from . import models, schemas

def get_producao(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Producao).offset(skip).limit(limit).all()

def get_processa_viniferas(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.ProcessaViniferas).offset(skip).limit(limit).all()
