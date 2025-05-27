from sqlalchemy.orm import Session
from sqlalchemy import and_, or_
from typing import *
from fastapi import Request, UploadFile, HTTPException
import models, schemas
import boto3

import jwt

import datetime

from pathlib import Path

async def get_collages_id(db: Session, id: int):

    collages_one = db.query(models.Collages).filter(models.Collages.id == id).first() 
    collages_one = collages_one.to_dict() if collages_one else collages_one

    res = {
        'collages_one': collages_one,
    }
    return res

async def post_collages(db: Session, raw_data: schemas.PostCollages):
    id:int = raw_data.id
    name:str = raw_data.name


    record_to_be_added = {'id': id, 'name': name}
    new_collages = models.Collages(**record_to_be_added)
    db.add(new_collages)
    db.commit()
    db.refresh(new_collages)
    collages_inserted_record = new_collages.to_dict()

    res = {
        'collages_inserted_record': collages_inserted_record,
    }
    return res

async def put_collages_id(db: Session, id: int, name: str):

    collages_edited_record = db.query(models.Collages).filter(models.Collages.id == id).first()
    for key, value in {'id': id, 'name': name}.items():
          setattr(collages_edited_record, key, value)
    db.commit()
    db.refresh(collages_edited_record)
    collages_edited_record = collages_edited_record.to_dict() 

    res = {
        'collages_edited_record': collages_edited_record,
    }
    return res

async def delete_collages_id(db: Session, id: int):

    collages_deleted = None
    record_to_delete = db.query(models.Collages).filter(models.Collages.id == id).first()

    if record_to_delete:
        db.delete(record_to_delete)
        db.commit()
        collages_deleted = record_to_delete.to_dict() 

    res = {
        'collages_deleted': collages_deleted,
    }
    return res

async def get_collages(db: Session):


    query = db.query(models.Collages)
    query = query.filter(
        
        and_(
            models.Collages.hello == str
        )
    )


    query = query.order_by(models.Collages.id.desc())


    query = query.limit(10)



    collages_all = query.all()
    collages_all = [new_data.to_dict for new_data in collages_all] if collages_all else collages_all

    res = {
        'collages_all': collages_all,
    }
    return res

