from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from .. import crud, schemas
from ..database import get_db

router = APIRouter(prefix="/invoices", tags=["invoices"])

@router.post("/student/{student_id}", response_model=schemas.Invoice)
def create_invoice(student_id: int, invoice: schemas.InvoiceCreate, db: Session = Depends(get_db)):
    return crud.create_invoice(db, invoice, student_id)

@router.get("/", response_model=list[schemas.Invoice])
def list_invoices(db: Session = Depends(get_db)):
    return crud.get_invoices(db)
