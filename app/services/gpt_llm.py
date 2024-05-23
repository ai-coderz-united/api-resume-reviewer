import os
from typing import Optional, Union

from dotenv import load_dotenv
from langchain_core.messages import (
	BaseMessage,
	HumanMessage,
	SystemMessage,
)
from langchain_openai import ChatOpenAI
from openai import APIError
from pydantic import BaseModel
from pydantic.v1 import SecretStr

from app.utils.logger import app_logger, log_exception

load_dotenv()


class GPTRequest(BaseModel):
	llm: Optional[ChatOpenAI] = None

	def setup_openai_gpt(self) -> None:
		app_logger.info("Setting up OpenAI GPT model.")
		key_value = os.getenv("OPENAI_API_KEY")
		model_name = os.getenv("OPENAI_MODEL_NAME")

		if key_value and model_name:
			self.llm = ChatOpenAI(
				model=model_name, temperature=0, api_key=SecretStr(key_value)
			)

	def send_to_gpt(self, resume_text: str) -> Union[BaseMessage, str, dict]:
		if self.llm is not None:
			app_logger.info("Sending resume text to OpenAI GPT model.")
			messages = [
				SystemMessage(content=self.read_systems_message()),
				HumanMessage(content=resume_text),
			]

			try:
				result = self.llm.invoke(messages)
				app_logger.info(f"Received response from OpenAI GPT model: {result}")
				return result
			except APIError as error:
				log_exception()
				app_logger.error(
					f"Error occurred while invoking OpenAI GPT model: {error}"
				)
				raise APIError(
					body={},
					message="Error occurred while invoking OpenAI GPT model.",
					request=error.request,
				)

		return "No LLM model available."

	def read_systems_message(self):
		try:
			with open("app/data/systems_message.txt", "r") as file:
				return file.read()
		except FileNotFoundError:
			log_exception()
			raise FileNotFoundError("Systems message file not found.")
