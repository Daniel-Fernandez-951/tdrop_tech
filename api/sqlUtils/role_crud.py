from fastapi import HTTPException, status
from sqlalchemy.orm import Session

from . import models
from .schema import schemas


# GET
def get_active_roles(db: Session):
    return db.query(models.Role).filter(models.Role.is_active == True).all()


def get_name_role(db: Session,
                  role_name: str):
    return db.query(models.Role).filter(models.Role.role_name == role_name).all()


# POST
def post_role(db: Session,
              role: schemas.RoleCreate,
              company_id: str):
    db_role = models.Role(**role.dict(), company_id=company_id)
    db.add(db_role)
    db.commit()
    db.refresh(db_role)
    return db_role


# PUT
def update_role(db: Session,
                request: schemas.RoleCreate,
                role_id: str = None):
    db_update = db.query(models.Role).filter(models.Role.id == role_id)
    status_up = db_update.update(request.__dict__)
    if status_up == 0:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"Role with id {role_id} not found")
    db.commit()
    return {"Updated"}


# DELETE
def delete_role(db: Session,
                role_id: str):
    db_delete = db.query(models.Role).filter(models.Role.id == role_id).first()

    if not db_delete:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"Role with id {role_id} not found")
    db.delete(db_delete)
    db.commit()
    return {'Deleted'}
