import json
import os
from typing import Optional

from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from openai import APIError
from pydantic import BaseModel
from pydantic.v1 import SecretStr

from app.utils.logger import app_logger, log_exception

load_dotenv()


class GPTExecutor(BaseModel):
	llm: Optional[ChatOpenAI] = None

	def setup_openai_gpt(self) -> None:
		app_logger.info("Setting up OpenAI GPT model.")
		key_value = os.getenv("OPENAI_API_KEY")
		model_name = os.getenv("OPENAI_MODEL_NAME")

		if key_value and model_name:
			self.llm = ChatOpenAI(
				model=model_name, temperature=0, api_key=SecretStr(key_value)
			)

	def call_llm(self, instructions: list) -> dict:
		if self.llm is None:
			raise ValueError("LLM is not set up. Please call setup_openai_gpt first.")
		try:
			llm_response = self.llm.invoke(instructions)
			if isinstance(llm_response.content, str):
				jsonified_resume: dict = json.loads(llm_response.content)
			else:
				raise ValueError("Response content is not a valid JSON string.")
			app_logger.info(
				f"Received response from OpenAI GPT model: {jsonified_resume}"
			)
			return jsonified_resume
		except json.JSONDecodeError as error:
			log_exception()
			app_logger.error(
				f"Error occurred while decoding OpenAI GPT model response: {error}"
			)
			raise json.JSONDecodeError(
				msg="Error occurred while decoding OpenAI GPT model response.",
				doc=error.doc,
				pos=error.pos,
			)
		except APIError as error:
			log_exception()
			app_logger.error(f"Error occurred while invoking OpenAI GPT model: {error}")
			raise APIError(
				body={},
				message="Error occurred while invoking OpenAI GPT model.",
				request=error.request,
			)

	def read_systems_message(self, systems_message_path: str) -> str:
		try:
			with open(systems_message_path, "r") as file:
				return file.read()
		except FileNotFoundError:
			log_exception()
			raise FileNotFoundError("Systems message file not found.")
