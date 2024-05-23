from fastapi import FastAPI

from app.routers import health, resume_review

app = FastAPI()

app.include_router(health.router)
app.include_router(resume_review.router)
