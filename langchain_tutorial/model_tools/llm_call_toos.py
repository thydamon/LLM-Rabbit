from langchain_core.messages import HumanMessage, ToolMessage

from langchain_tutorial.base.LLMFactory import LLMFactory
from langchain_tutorial.model_tools import function_tools
from langchain_tutorial.model_tools.function_tools import add, multiply

query = "What is 3 * 12? Also, what is 11 + 49?"
# 1. 用户提问
messages = [HumanMessage(query)]
llm = LLMFactory.get_llm()
llm_with_tools = llm.bind_tools(function_tools.tools)

# 2. AI恢复并请求工具调用
ai_msg = llm_with_tools.invoke(messages)
# print(ai_msg)
# Append the AI message to the message list
messages.append(ai_msg)

# 3. 工具调用并生成ToolMessage
for tool_call in ai_msg.tool_calls:
    selected_tool = {"add": add, "multiply": multiply}[tool_call["name"].lower()]
    args = tool_call["args"]
    result = selected_tool(**args)
    tool_msg = ToolMessage(
        tool_call_id=tool_call["id"],
        content=result
    )
    messages.append(tool_msg)

# 4. 再次调用LLM，获得最终回复
# print(messages)
result = llm_with_tools.invoke(messages)
print(result)

# Call the tools with the AI message
# tool_calls = llm_with_tools.invoke_tool(messages)
# print(tool_calls)