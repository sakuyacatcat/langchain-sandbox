from langchain.document_loaders import GitLoader
from langchain.text_splitter import CharacterTextSplitter
from langchain.vectorstores import Chroma
from langchain_huggingface.embeddings import HuggingFaceEmbeddings


def file_filter(file_path):
    return file_path.endswith(".py")


loader = GitLoader(
    clone_url="https://github.com/sakuyacatcat/langchain-sandbox",
    repo_path="./sandbox",
    branch="main",
    file_filter=file_filter,
)

raw_docs = loader.load()

text_splitter = CharacterTextSplitter(chunk_size=10, chunk_overlap=0)
splitted_docs = text_splitter.split_documents(raw_docs)

embeddings = HuggingFaceEmbeddings(model_name="sentence-transformers/all-mpnet-base-v2")
db = Chroma.from_documents(splitted_docs, embeddings)
retriever = db.as_retriever()

query = "PromptTemplateの使い方を教えて下さい。"
context_docs = retriever.get_relevant_documents(query)

print(context_docs[0].page_content)
