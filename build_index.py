from ingestion.loader import load_documents
from ingestion.chunker import chunk_documents
from ingestion.indexer import build_index

DATA_DIR = "data/laptop_docs"

docs = load_documents(DATA_DIR)
chunks = chunk_documents(docs)
build_index(chunks)

print("✅ Vector index built successfully")
