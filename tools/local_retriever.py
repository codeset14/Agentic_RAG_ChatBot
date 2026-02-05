from ingestion.indexer import load_index

class LocalRetrieverTool:
    def __init__(self):
        vectorstore = load_index()
        self.retriever = vectorstore.as_retriever(search_kwargs={"k": 4})

    def run(self, query: str) -> str:
        docs = self.retriever.invoke(query)
        return "\n\n".join(doc.page_content for doc in docs)
