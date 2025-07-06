import sys
import os
from langchain_tutorial.model_tools import function_tools, pydantic_tools, typedicts_tools

# 导入langchain_tutorial的路径
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../../..')))
from langchain_tutorial.base.LLMFactory import LLMFactory

llm = LLMFactory.get_llm()
# function_tools
# llm_with_toos = llm.bind_tools(function_tools.tools)
# pydantic_tools
# llm_with_toos = llm.bind_tools(pydantic_tools.tools)
llm_with_toos = llm.bind_tools(typedicts_tools.tools)
query = "What is 3 * 12?"
result = llm_with_toos.invoke(query)
print(result)