from langchain.document_loaders import GitLoader


def file_filter(file_path):
    return file_path.endswith(".py")


loader = GitLoader(
    clone_url="https://github.com/sakuyacatcat/langchain-sandbox",
    repo_path="./sandbox",
    branch="main",
    file_filter=file_filter,
)

raw_docs = loader.load()

print(len(raw_docs))
