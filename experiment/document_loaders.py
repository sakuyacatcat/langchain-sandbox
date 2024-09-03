from langchain.document_loaders import GitLoader
from langchain.text_splitter import CharacterTextSplitter


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
print(len(splitted_docs))
