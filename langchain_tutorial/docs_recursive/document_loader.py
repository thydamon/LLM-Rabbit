from langchain_community.document_loaders import TextLoader
from langchain_community.document_loaders import CSVLoader
from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import CharacterTextSplitter, RecursiveCharacterTextSplitter
from dotenv import load_dotenv
import os
from doctran_upgrade.doctran import Doctran


# textLoader = TextLoader(file_path="../data/test.md", encoding="utf-8")
# textLoader.load()
#
# csvLoader = CSVLoader(file_path="../data/test.csv", encoding="utf-8")
# csvLoader.load()

# pdfLoader = PyPDFLoader(file_path="../data/test.pdf")
# pdfLoader.load()

# 文档加载
content = None
with open("langchain_tutorial/data/sample-multilingual-text.pdf", "r", encoding='utf-8', errors='ignore') as file:
    content = file.read()

load_dotenv("langchain_tutorial/base/openai.env")

doctrans = Doctran(
    openai_api_key=os.environ.get("OPENAI_API_KEY"),
    openai_model=os.environ.get("OPENAI_MODEL"),
    openai_token_limit=os.environ.get("OPENAI_TOKEN_LIMIT"),
    openai_base_url=os.environ.get("OPENAI_API_BASE")
)

documents = doctrans.parse(content=content)
# 总结文档
summary = documents.summarize(token_limit=os.environ.get("TOKEN_LIMIT"))
print(summary)