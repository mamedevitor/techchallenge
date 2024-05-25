from sqlalchemy.orm import Session
from app import models

def get_producao(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Producao).offset(skip).limit(limit).all()

def get_processa_viniferas(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.ProcessaViniferas).offset(skip).limit(limit).all()

def get_processa_uvamesa(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.ProcessaUvaMesa).offset(skip).limit(limit).all()

def get_processa_semclassf(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.ProcessaSemClassf).offset(skip).limit(limit).all()

def get_processa_americanashibridas(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.ProcessaAmericanasHibridas).offset(skip).limit(limit).all()

def get_importacao_vinhos(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.ImportacaoVinhos).offset(skip).limit(limit).all()

def get_importacao_uvaspassas(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.ImportacaoUvasPassas).offset(skip).limit(limit).all()

def get_importacao_uvasfrescas(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.ImportacaoUvasFrescas).offset(skip).limit(limit).all()

def get_importacao_suco(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.ImportacaoSuco).offset(skip).limit(limit).all()

def get_importacao_espumantes(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.ImportacaoEspumantes).offset(skip).limit(limit).all()

def get_exportacao_vinhomesa(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.ExportacaoVinhoMesa).offset(skip).limit(limit).all()

def get_exportacao_uvasfrescas(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.ExportacaoUvasFrescas).offset(skip).limit(limit).all()

def get_exportacao_suco(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.ExportacaoSuco).offset(skip).limit(limit).all()

def get_exportacao_espumantes(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.ExportacaoEspumantes).offset(skip).limit(limit).all()

def get_comercio(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Comercio).offset(skip).limit(limit).all()
