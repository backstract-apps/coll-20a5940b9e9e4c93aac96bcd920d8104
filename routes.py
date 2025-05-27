from fastapi import APIRouter, Request, Depends, HTTPException, UploadFile, Form
from sqlalchemy.orm import Session
from typing import List
import service, models, schemas
from database import SessionLocal, engine

models.Base.metadata.create_all(bind=engine)

router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.get('/collages/id')
async def get_collages_id(id: int, db: Session = Depends(get_db)):
    try:
        return await service.get_collages_id(db, id)
    except Exception as e:
        raise HTTPException(500, str(e))

@router.post('/collages/')
async def post_collages(raw_data: schemas.PostCollages, db: Session = Depends(get_db)):
    try:
        return await service.post_collages(db, raw_data)
    except Exception as e:
        raise HTTPException(500, str(e))

@router.put('/collages/id/')
async def put_collages_id(id: int, name: str, db: Session = Depends(get_db)):
    try:
        return await service.put_collages_id(db, id, name)
    except Exception as e:
        raise HTTPException(500, str(e))

@router.delete('/collages/id')
async def delete_collages_id(id: int, db: Session = Depends(get_db)):
    try:
        return await service.delete_collages_id(db, id)
    except Exception as e:
        raise HTTPException(500, str(e))

@router.get('/collages/')
async def get_collages(db: Session = Depends(get_db)):
    try:
        return await service.get_collages(db)
    except Exception as e:
        raise HTTPException(500, str(e))

