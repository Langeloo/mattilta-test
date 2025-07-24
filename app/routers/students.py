from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from .. import crud, schemas
from ..database import get_db

router = APIRouter(prefix="/students", tags=["students"])

@router.post("/", response_model=schemas.Student)
def create_student(student: schemas.StudentCreate, db: Session = Depends(get_db)):
    return crud.create_student(db, student)

@router.get("/", response_model=list[schemas.Student])
def list_students(db: Session = Depends(get_db)):
    return crud.get_students(db)
