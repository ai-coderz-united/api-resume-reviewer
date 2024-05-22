from fastapi import APIRouter

router = APIRouter(
	prefix="/api",
	tags=["health"],
	responses={404: {"description": "Not found"}},
)


@router.get("/ping")
async def root():
	return {"status": "healthy"}
