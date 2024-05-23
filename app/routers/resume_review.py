from fastapi import APIRouter, UploadFile
from fastapi.responses import JSONResponse
from pydantic import ValidationError

from app.models.resume_review import PDFResume
from app.services.gpt_llm import GPTRequest
from app.services.resume_parser import ResumeParser

router = APIRouter(
	prefix="/api",
	tags=["reviewer"],
	responses={404: {"description": "Not found"}},
)


@router.post("/resume/review")
async def resume_review(file: UploadFile):
	try:
		pdf_resume = PDFResume(resume=file)

		# parse the pdf resume
		pdf_text = ResumeParser().extract_text_from_pdf(await pdf_resume.resume.read())

		# send text to GPT to have structured data extracted (JSON)
		gpt_handler = GPTRequest()
		gpt_handler.setup_openai_gpt()
		gpt_response = gpt_handler.send_to_gpt(pdf_text)

		# send to GPT for review and recommendations of the resume

		# return the resume text and the recommendations

	except ValidationError as e:
		return JSONResponse(status_code=400, content={"detail": str(e)})
	except Exception as e:
		return JSONResponse(status_code=500, content={"detail": str(e)})

	return {
		"filename": file.filename,
		"text": pdf_text,
		"gpt_foramtted_resume": gpt_response,
	}
