from langchain_core.messages import SystemMessage
from langchain_core.prompts import ChatPromptTemplate

chat_template = ChatPromptTemplate.from_messages(
    [
        ("system","你是一个起名大师,你的名字叫{name}"),
        ("user" "你好{name},你感觉如何？"),
        ("ai" "你好！我状态非常好！"),
        ("human", "{user_input}")
    ]
)

chat_template.from_template(name="陈大师", user_input="请给我起个名字?")

# 直接创建消息
SystemMessage(
    content="你是一个起名大师",
    addition_kwargs={"name": "陈大师"}
)



