from rag.llm import get_llm
from tools.local_retriever import LocalRetrieverTool
from langchain.schema import HumanMessage

class RAGPipeline:
    def __init__(self):
        self.llm = get_llm()
        self.retriever = LocalRetrieverTool()

    def run(self, query: str) -> str:
        context = self.retriever.run(query)

        prompt = f"""
Answer the question using ONLY the context below.

Context:
{context}

Question:
{query}
"""

        response = self.llm.invoke(
            [HumanMessage(content=prompt)]
        )

        return response.content
