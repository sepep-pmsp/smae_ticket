from fastapi import APIRouter, Query

from typing import List, Union

from fastapi import Depends, HTTPException
from sqlalchemy.orm import Session

from core.dao import basic as basicdao
from core.dao import filtros, get_db
from core.models import basic as basicmodels
from core.schemas import basic as basicschemas
from core.models.database import SessionLocal, engine

basicmodels.Base.metadata.create_all(bind=engine)

app = APIRouter()

NIVEIS_REGIOES = filtros.nomes_niveis()
TEMAS = filtros.nomes_temas()

@app.get("/temas/", response_model=List[basicschemas.TemaSimples], tags=['Indicadores'])
def read_indicadores(db: Session = Depends(get_db)):

    temas = basicdao.list_temas(db)
    return temas
