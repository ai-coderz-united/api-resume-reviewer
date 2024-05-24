import json
from typing import Union

from dotenv import load_dotenv
from langchain_core.messages import (
	BaseMessage,
	HumanMessage,
	SystemMessage,
)
from pydantic import BaseModel

from app.services.gpt_executor import GPTExecutor
from app.utils.logger import app_logger

load_dotenv()


class ResumeReview(BaseModel):
	gpt_executor: GPTExecutor

	def resume_parsing(self, resume_text: str) -> Union[BaseMessage, str, dict]:
		if self.gpt_executor.llm is not None:
			app_logger.info("Sending resume text to OpenAI GPT model.")
			messages = [
				SystemMessage(
					content=self.gpt_executor.read_systems_message(
						"app/data/resume_parsing_sm.txt"
					)
				),
				HumanMessage(content=resume_text),
			]
			return self.gpt_executor.call_llm(messages)

		return "No LLM model available."

	def resume_recommendations(
		self, resume_dictionary: dict, job_title: str, company_name: str
	) -> Union[BaseMessage, str, dict]:
		if self.gpt_executor.llm is not None:
			resume_dictionary["desired_job_title"] = job_title
			resume_dictionary["desired_company_name"] = company_name

			app_logger.info(
				"Sending resume dictionary to OpenAI GPT model for recommendations."
			)
			messages = [
				SystemMessage(
					content=self.gpt_executor.read_systems_message(
						"app/data/resume_recommendations_sm.txt"
					)
				),
				HumanMessage(content=json.dumps(resume_dictionary)),
			]
			return self.gpt_executor.call_llm(messages)

		return "No LLM model available."
