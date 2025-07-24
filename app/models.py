from sqlalchemy import Column, Integer, String, ForeignKey, Float
from sqlalchemy.orm import relationship
from .database import Base

class School(Base):
    __tablename__ = "schools"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, unique=True, index=True)
    address = Column(String)

    students = relationship("Student", back_populates="school")

class Student(Base):
    __tablename__ = "students"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    school_id = Column(Integer, ForeignKey("schools.id"))

    school = relationship("School", back_populates="students")
    invoices = relationship("Invoice", back_populates="student")

class Invoice(Base):
    __tablename__ = "invoices"

    id = Column(Integer, primary_key=True, index=True)
    amount = Column(Float)
    student_id = Column(Integer, ForeignKey("students.id"))

    student = relationship("Student", back_populates="invoices")
