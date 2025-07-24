from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from .. import crud, schemas
from ..database import get_db

router = APIRouter(prefix="/schools", tags=["schools"])

@router.post("/", response_model=schemas.School)
def create_school(school: schemas.SchoolCreate, db: Session = Depends(get_db)):
    return crud.create_school(db, school)

@router.get("/", response_model=list[schemas.School])
def list_schools(db: Session = Depends(get_db)):
    return crud.get_schools(db)
