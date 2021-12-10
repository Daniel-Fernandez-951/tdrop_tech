from uuid import UUID
from pydantic import BaseModel
from typing import Optional, List
from datetime import date


# ROLE Schemas
class RoleBase(BaseModel):
    role_name: str
    bounty: int
    is_active: bool = True


class RoleCreate(RoleBase):
    pass


class Role(RoleBase):
    id: UUID
    company_id: UUID
    role_date: date
    
    class Config:
        orm_mode = True


# COMPANY Schemas
class CompanyBase(BaseModel):
    name: str
    funding_stage: Optional[str]
    is_active: Optional[bool] = True


class CompanyCreate(CompanyBase):
    pass


class Company(CompanyBase):
    id: UUID
    roles: List[Role] = []

    class Config:
        orm_mode = True
