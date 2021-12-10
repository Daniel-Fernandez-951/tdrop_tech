from fastapi import FastAPI
from api.sqlUtils.models import Base
from api.sqlUtils.database import engine
from core import company_router, role_router


Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="Talentdrop Technical",
    version="0.0.1",
)

app.include_router(company_router.router)
app.include_router(role_router.router)

