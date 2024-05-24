from fastapi import APIRouter, UploadFile
from fastapi.responses import JSONResponse
from pydantic import ValidationError

from app.models.resume_review import PDFResume
from app.services.gpt_executor import GPTExecutor
from app.services.resume_parser import ResumeParser
from app.services.resume_review import ResumeReview

router = APIRouter(
	prefix="/api",
	tags=["reviewer"],
	responses={404: {"description": "Not found"}},
)


@router.post("/resume/review")
async def resume_review(file: UploadFile):
	try:
		pdf_resume = PDFResume(resume=file)
		pdf_text = ResumeParser().extract_text_from_pdf(await pdf_resume.resume.read())
		gpt_handler = GPTExecutor()
		gpt_handler.setup_openai_gpt()
		resume_review = ResumeReview(gpt_executor=gpt_handler)
		jsonified_resume = resume_review.resume_parsing(pdf_text)
		resume_recommendations = resume_review.resume_recommendations(jsonified_resume)
	except ValidationError as e:
		return JSONResponse(status_code=400, content={"detail": str(e)})
	except Exception as e:
		return JSONResponse(status_code=500, content={"detail": str(e)})

	return {
		"filename": file.filename,
		"original_resume": jsonified_resume,
		"resume_recommendations": resume_recommendations,
	}
