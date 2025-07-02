from langchain_core.vectorstores import InMemoryVectorStore
from langchain_openai import OpenAIEmbeddings

from docs_recursive.pdf_document_recursive import PDFDocumentRecursive

pdf_document_recursive = PDFDocumentRecursive(file_path="../data/test.pdf")
docs = pdf_document_recursive.split_documents_recursive(chunk_size=100, chunk_overlap=0)

# embeddings_model = OpenAIEmbeddings()
# 嵌入多个文档
# embeddings = embeddings_model.embed_documents(docs)
# 嵌入单个文档(查询)
# query_embedding = embeddings_model.embed_query("请问这篇文档的主要内容是什么？")
# 向量存储
embeddings_model = OpenAIEmbeddings(
    model="text-embedding-3-large",
    openai_api_key="sk-GkNYi13AfyobCns4OaLDn7x6ECg2w8Be2LYeZsuUKsCdtChn",
    openai_api_base="https://api.chatanywhere.tech"
)
vector_stores = InMemoryVectorStore(embeddings_model)
vector_stores.add_documents(documents=docs)

# 向量数据库检索
results = vector_stores.similarity_search("词汇agents的含义是什么?")
print("向量搜索结果:{}", results)
