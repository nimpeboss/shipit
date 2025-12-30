from sqlalchemy.orm import Session
from .models import Project

def get_projects(db: Session):
    return db.query(Project).all()

def create_projrct(db: Session, name: str, description: str):
    project = Project(name=name, description=description)
    db.add(project)
    db.commit()
    db.refresh(project)
    return project
