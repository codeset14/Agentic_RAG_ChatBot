import os
from langchain_community.document_loaders import PyPDFLoader, TextLoader

def load_documents(data_dir: str):
    documents = []

    for file in os.listdir(data_dir):
        path = os.path.join(data_dir, file)

        if file.endswith(".pdf"):
            documents.extend(PyPDFLoader(path).load())

        elif file.endswith(".txt"):
            documents.extend(TextLoader(path, encoding="utf-8").load())

    return documents
