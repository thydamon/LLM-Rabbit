from langchain_deepseek import ChatDeepSeek
from langchain_openai.chat_models.base import BaseChatOpenAI
import os

class LLMFactory:

    api_base = os.getenv("DEEPSEEK_API_BASE", "https://api.deepseek.com/v1")
    api_key = os.getenv("DEEPSEEK_API_KEY", "sk-4b684211e8d0471390a2e3ed3c941b6c")

    @staticmethod
    def get_llm():
        return BaseChatOpenAI(
            model="deepseek-chat",
            temperature=0,
            openai_api_key=LLMFactory.api_key,
            openai_api_base=LLMFactory.api_base,
            max_tokens=1024
        )

    @staticmethod
    def get_deepseek_llm():
        return ChatDeepSeek(
            model="deepseek-chat",
            temperature=0,
            api_key=LLMFactory.api_key,
            api_base=LLMFactory.api_base,
            max_tokens=1024,
            max_retries=2
        )