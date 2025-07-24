from fastapi import FastAPI
from .database import Base, engine
from .routers import schools, students, invoices

Base.metadata.create_all(bind=engine)

app = FastAPI()

app.include_router(schools.router)
app.include_router(students.router)
app.include_router(invoices.router)
