import uuid
import datetime
from .database import Base
from sqlalchemy.orm import relationship
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy import Column, Integer, String, ForeignKey, Boolean, Date


def _date_now():
    return datetime.datetime.now().date()


class Company(Base):
    __tablename__ = "companies"
    id = Column(UUID(as_uuid=True), primary_key=True,
                index=True, default=uuid.uuid4,
                nullable=False, autoincrement=False,
                unique=True)
    name = Column(String, nullable=False, unique=True)
    funding_stage = Column(String, nullable=False)
    is_active = Column(Boolean, default=True, index=True)
    roles = relationship("Role", backref="companies")


class Role(Base):
    __tablename__ = "roles"
    id = Column(UUID(as_uuid=True), primary_key=True,
                index=True, default=uuid.uuid4,
                nullable=False, autoincrement=False,
                unique=True)
    company_id = Column(UUID, ForeignKey('companies.id'))
    role_name = Column(String, nullable=False)
    bounty = Column(Integer, nullable=False)
    role_date = Column(Date, default=_date_now)
    is_active = Column(Boolean, default=True, index=True)


