from langchain.document_loaders import TextLoader
from langchain.document_loaders import CSVLoader
from langchain.document_loaders import PyPDFLoader
from langchain_text_splitters import CharacterTextSplitter, RecursiveCharacterTextSplitter
from dotenv import load_dotenv
import os
from doctran import Doctran


# textLoader = TextLoader(file_path="../data/test.md", encoding="utf-8")
# textLoader.load()
#
# csvLoader = CSVLoader(file_path="../data/test.csv", encoding="utf-8")
# csvLoader.load()

# pdfLoader = PyPDFLoader(file_path="../data/test.pdf")
# pdfLoader.load()

# 文档加载
content = None
with open("../data/test.md", "r", encoding="utf-8") as file:
    content = file.read()



doctrans = Doctran(

)