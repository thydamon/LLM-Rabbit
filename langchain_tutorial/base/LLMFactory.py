from dotenv import load_dotenv
from langchain_deepseek import ChatDeepSeek
from langchain_openai.chat_models.base import BaseChatOpenAI
import os

load_dotenv("openai.env")

class LLMFactory:

    api_base = os.environ.get("OPEN_API_BASE")
    api_key = os.environ.get("OPEN_API_KEY")

    @staticmethod
    def get_llm():
        return BaseChatOpenAI(
            model=os.environ.get("OPENAI_MODEL"),
            temperature=0,
            openai_api_key=LLMFactory.api_key,
            openai_api_base=LLMFactory.api_base,
            max_tokens=os.environ.get("OPENAI_TOKEN_LIMIT"),
        )

    @staticmethod
    def get_deepseek_llm():
        return ChatDeepSeek(
            model=os.environ.get("OPENAI_MODEL"),
            temperature=0,
            api_key=LLMFactory.api_key,
            api_base=LLMFactory.api_base,
            max_tokens=os.environ.get("OPENAI_TOKEN_LIMIT"),
            max_retries=2
        )
