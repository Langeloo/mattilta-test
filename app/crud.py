from sqlalchemy.orm import Session
from . import models, schemas

def create_school(db: Session, school: schemas.SchoolCreate):
    db_school = models.School(**school.dict())
    db.add(db_school)
    db.commit()
    db.refresh(db_school)
    return db_school

def create_student(db: Session, student: schemas.StudentCreate):
    db_student = models.Student(**student.dict())
    db.add(db_student)
    db.commit()
    db.refresh(db_student)
    return db_student

def create_invoice(db: Session, invoice: schemas.InvoiceCreate, student_id: int):
    db_invoice = models.Invoice(**invoice.dict(), student_id=student_id)
    db.add(db_invoice)
    db.commit()
    db.refresh(db_invoice)
    return db_invoice

def get_schools(db: Session):
    return db.query(models.School).all()

def get_students(db: Session):
    return db.query(models.Student).all()

def get_invoices(db: Session):
    return db.query(models.Invoice).all()
