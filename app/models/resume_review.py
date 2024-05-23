from fastapi import UploadFile
from pydantic import BaseModel, field_validator


class PDFResume(BaseModel):
	resume: UploadFile

	@field_validator("resume")
	def validate_pdf(cls, v):
		if v.content_type != "application/pdf" or not v.filename.endswith(".pdf"):
			raise ValueError("Only PDF files are allowed")
		return v
