from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session
from api.sqlUtils.schema import schemas
from api.sqlUtils import database, company_crud
from typing import List


router = APIRouter(tags=["Company"], prefix="/company")
get_db = database.get_db


# GET
@router.get("/active/",
            status_code=status.HTTP_200_OK,
            response_model=List[schemas.Company],
            description="Get all ACTIVE companies")
def get_active_companies(db: Session = Depends(get_db)):
    return company_crud.get_active_companies(db=db)


@router.get("/{name}",
            status_code=status.HTTP_200_OK,
            response_model=schemas.Company,
            description="Get company by name")
def get_company_by_name(name: str,
                        db: Session = Depends(get_db)):
    return company_crud.get_name_company(db=db,
                                         name=name)


@router.get("/funding/{funding_stage}",
            status_code=status.HTTP_200_OK,
            response_model=List[schemas.Company],
            description="Get companies by funding stage")
def get_companies_by_funding(funding_stage: str,
                             db: Session = Depends(get_db)):
    return company_crud.get_funding_companies(db=db,
                                              funding_stage=funding_stage)


# POST
@router.post("/new/",
             status_code=status.HTTP_201_CREATED,
             response_model=schemas.Company,
             description="Create a company")
def post_company(request: schemas.CompanyCreate,
                 db: Session = Depends(get_db)):
    return company_crud.post_company(db=db,
                                     company=request)


# PUT
@router.put("/up/{company_id}",
            status_code=status.HTTP_202_ACCEPTED,
            description="Update a company by ID")
def put_company(company_id: str,
                request: schemas.CompanyCreate,
                db: Session = Depends(get_db)):
    return company_crud.update_company(db=db,
                                       company_id=company_id,
                                       request=request)


# DELETE
@router.delete("/del/{company_id}",
               status_code=status.HTTP_202_ACCEPTED,
               description="Remove a company by ID")
def remove_company(company_id: str,
                   db: Session = Depends(get_db)):
    return company_crud.delete_company(db=db,
                                       company_id=company_id)
