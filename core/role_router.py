from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session
from api.sqlUtils.schema import schemas
from api.sqlUtils import database, role_crud
from typing import List


router = APIRouter(tags=["Role"], prefix="/role")
get_db = database.get_db


# GET Role
@router.get("/active/",
            status_code=status.HTTP_200_OK,
            response_model=List[schemas.Role],
            description="Get all ACTIVE roles")
def get_active(db: Session = Depends(get_db)):
    return role_crud.get_active_roles(db=db)


@router.get("/{role_name}",
            status_code=status.HTTP_200_OK,
            response_model=List[schemas.Role],
            description="Get all roles by name")
def get_role_by_name(role_name: str,
                     db: Session = Depends(get_db)):
    return role_crud.get_name_role(db=db,
                                   role_name=role_name)


# CREATE Role
@router.post("/new/{company_id}",
             status_code=status.HTTP_201_CREATED,
             response_model=schemas.Role,
             description="Create a role")
def create_role(request: schemas.RoleCreate,
                company_id: str,
                db: Session = Depends(get_db)):
    return role_crud.post_role(db=db, role=request, company_id=company_id)


# PUT
@router.put("/up/{role_id}",
            status_code=status.HTTP_202_ACCEPTED,
            description="Update a role by ID")
def put_role(role_id: str,
             request: schemas.RoleCreate,
             db: Session = Depends(get_db)):
    return role_crud.update_role(db=db,
                                 role_id=role_id,
                                 request=request)


# DELETE
@router.delete("/del/{role_id}",
               status_code=status.HTTP_202_ACCEPTED,
               description="Delete a role by ID")
def remove_role(role_id: str,
                db: Session = Depends(get_db)):
    return role_crud.delete_role(db=db,
                                 role_id=role_id)
