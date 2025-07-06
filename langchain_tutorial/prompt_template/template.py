from langchain_core.prompts import PromptTemplate
from langchain_tutorial.base.LLMFactory import LLMFactory

llm = LLMFactory.get_llm()
prompt = PromptTemplate.from_template("你是一个起名大师,请模仿示例起3个{country}名字,比如男孩经常被叫做{boy},女孩经常被叫做{girl}")
message = prompt.format(country="中国特色的",boy="狗蛋",girl="翠花")
result = llm.invoke(message)
print(result)