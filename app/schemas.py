from pydantic import BaseModel
from typing import List, Optional

class InvoiceBase(BaseModel):
    amount: float

class InvoiceCreate(InvoiceBase):
    pass

class Invoice(InvoiceBase):
    id: int
    class Config:
        orm_mode = True

class StudentBase(BaseModel):
    name: str

class StudentCreate(StudentBase):
    school_id: int

class Student(StudentBase):
    id: int
    invoices: List[Invoice] = []
    class Config:
        orm_mode = True

class SchoolBase(BaseModel):
    name: str
    address: str

class SchoolCreate(SchoolBase):
    pass

class School(SchoolBase):
    id: int
    students: List[Student] = []
    class Config:
        orm_mode = True
