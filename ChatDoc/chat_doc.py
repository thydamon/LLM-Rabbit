from langchain.document_loaders import Docx2txtLoader, PyPDFLoader
from langchain.text_splitter import CharacterTextSplitter
from langchain.embeddings import OpenAIEmbeddings
from langchain_community.vectorstores import Chroma
from langchain.chat_models import ChatOpenAI
from langchain.retrievers.multi_query import MultiQueryRetriever
from langchain.llms import OpenAI
from langchain.retrievers import ContextualCompressionRetriever
from langchain.retrievers.document_compressors import LLMChainExtractor


class ChatDoc:

    def __init__(self, doc):
        """
        Initializes the ChatDoc with a document path.

        :param doc: Path to the document file (e.g., .docx or .pdf).
        """
        self.doc = doc
        self.split_text = None

    def get_file(self):
        """
        Loads the document based on its file type.
        :return:
        """
        doc = self.doc
        loaders = {
            'docx': Docx2txtLoader,
            'pdf': PyPDFLoader
        }

        file_extension = doc.split('.')[-1]
        loader_class = loaders.get(file_extension)

        if loader_class:
            try:
                loader = loader_class(doc)
                text = loader.load()
                return text
            except Exception as e:
                print(f"Error loading {file_extension.upper()} file: {e}")
                return None
        else:
            print(f"Unsupported file type: {file_extension}")
            return None

    # 处理文档的函数
    def split_sentences(self):
        """
        Splits the document text into sentences or chunks.
        :param:
        :return:
        """
        full_text = self.get_file()
        if full_text:
            # 对文档进行分割
            text_splitter = CharacterTextSplitter(chunk_size=1000, chunk_overlap=200)
            texts = text_splitter.split_documents(full_text)
            self.split_text = texts

    # 向量化与向量存储
    def embedding_vectory_db(self):
        """
        Embeds the split text and stores it in a vector database.
        :return:
        """
        if self.split_text is None:
            print("No text to embed. Please split the document first.")
            return None

        embeddings_model = OpenAIEmbeddings()
        db = Chroma.from_documents(
            documents=self.split_text,
            embedding=embeddings_model,
            persist_directory="chroma_db"
        )

        return db

    # 并找到相关的文本块
    def ask_question(self, question):
        """
        Asks a question and retrieves relevant text blocks from the vector database.
        :param question: The question to ask.
        :return: Relevant text blocks.
        """
        if self.split_text is None:
            print("No text to search. Please split the document first.")
            return None

        db = self.embedding_vectory_db()
        retriever = db.as_retriever()
        llm = OpenAI(model="gpt-4", temperature=0.0)
        compressor = LLMChainExtractor.from_llm(llm=llm)
        compressor_retriever = ContextualCompressionRetriever(
            base_compressor=compressor,
            retriever=retriever
        )

        return compressor_retriever.get_relevant_documents(question)


        # llm = ChatOpenAI(model="gpt-4", temperature=0.0)
        # retriever_from_llm = MultiQueryRetriever.from_llm(
        #     llm=llm,
        #     retriever=db.as_retriever(),
        #     max_queries_per_question=3
        # )
        #
        # return retriever_from_llm.get_relevant_documents(question)

        # if db:
        #     results = db.similarity_search(question)
        #     return results
        # else:
        #     print("Failed to create vector database.")
        #     return None

    # 使用上下文压缩检索降低冗余信息
