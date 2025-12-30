from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session

from .db import Base, engine, SessionLocal
from . import crud

Base.metadata.create_all(bind=engine)

app = FastAPI(title="ShipIt API")

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.get("/health")
def health():
    return {"status": "ok"}

@app.get("/projects")
def list_projects(db: Session = Depends(get_db)):
    return crud.get_projects(db)

@app.post("/projects")
def add_project(name: str, description: str, db: Session = Depends(get_db)):
    return crud.create_projrct(db, name, description)