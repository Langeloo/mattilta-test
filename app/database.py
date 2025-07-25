from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base
from sqlalchemy.orm import Session

SQLALCHEMY_DATABASE_URL = "sqlite:///./school.db"

engine = create_engine(
    SQLALCHEMY_DATABASE_URL,
    connect_args={"check_same_thread": False}  # Solo para SQLite
)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()

# ✅ Esta función es clave para FastAPI
def get_db():
    db: Session = SessionLocal()
    try:
        yield db
    finally:
        db.close()
