from sqlalchemy.orm import Session
from fastapi import HTTPException, status

from . import models
from .schema import schemas


# GET
def get_active_companies(db: Session):
    return db.query(models.Company).filter(models.Company.is_active == True).all()


def get_name_company(db: Session,
                     name: str):
    return db.query(models.Company).filter(models.Company.name == name).first()


def get_funding_companies(db: Session,
                          funding_stage: str):
    return db.query(models.Company).filter(models.Company.funding_stage == funding_stage).all()


# POST
def post_company(db: Session,
                 company: schemas.CompanyCreate):
    db_company = models.Company(**company.dict())
    db.add(db_company)
    db.commit()
    db.refresh(db_company)
    return db_company


# PUT
def update_company(db: Session,
                   request: schemas.CompanyCreate,
                   company_id: str = None):
    db_update = db.query(models.Company).filter(models.Company.id == company_id)
    status_up = db_update.update(request.__dict__)
    if status_up == 0:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"Company with id {company_id} not found")
    db.commit()
    return {"Updated"}


# DELETE
def delete_company(db: Session,
                   company_id: str = None):
    db_delete = db.query(models.Company).filter(models.Company.id == company_id).first()

    if not db_delete:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"Company with id {company_id} not found")
    db.delete(db_delete)
    db.commit()
    return {'Deleted'}
