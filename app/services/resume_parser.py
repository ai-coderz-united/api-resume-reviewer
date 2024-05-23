import fitz
from pydantic import BaseModel


class ResumeParser(BaseModel):
	resume_text: str = ""

	def extract_text_from_pdf(self, resume_file: bytes) -> str:
		with fitz.open(stream=resume_file, filetype="pdf") as pdf:
			for page in pdf:
				self.resume_text += page.get_text()

		return self.resume_text
