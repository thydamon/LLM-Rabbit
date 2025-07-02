from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import CharacterTextSplitter, RecursiveCharacterTextSplitter

# file_path = "../data/test.pdf"
# loader = PyPDFLoader(file_path)

# docs = loader.load()
# print(len(docs))
# print(docs[0].page_content[:100])
# print(docs[0].metadata)
#
# # 基于长度分割
# text_splitter = CharacterTextSplitter.from_tiktoken_encoder(
#     encoding_name="cl100k_base",
#     chunk_size=100,
#     chunk_overlap=0
# )
# texts = text_splitter.split_documents(docs)
# print("基于长度:{}", texts[0])
#
# # 基于文档结构
# text_splitter = RecursiveCharacterTextSplitter(
#     chunk_size=100,
#     chunk_overlap=0,
#     add_start_index=True
# )
# texts = text_splitter.split_documents(docs)
# print("基于文档结构:{}", texts[0])

class PDFDocumentRecursive:

    def __init__(self, file_path):
        self.file_path = file_path
        self.loader = PyPDFLoader(file_path)
        self.docs = self.loader.load()
        self.texts = []

    def split_documents_recursive(self, chunk_size=100, chunk_overlap=0):
        text_splitter = RecursiveCharacterTextSplitter(
            chunk_size=chunk_size,
            chunk_overlap=chunk_overlap,
            add_start_index=True
        )
        self.texts = text_splitter.split_documents(self.docs)
        return self.texts