from langchain_community.vectorstores import FAISS
from ingestion.embedder import get_embeddings

def build_index(chunks, index_path="vectorstore"):
    embeddings = get_embeddings()
    vectorstore = FAISS.from_documents(chunks, embeddings)
    vectorstore.save_local(index_path)

def load_index(index_path="vectorstore"):
    embeddings = get_embeddings()
    return FAISS.load_local(
        index_path,
        embeddings,
        allow_dangerous_deserialization=True
    )
