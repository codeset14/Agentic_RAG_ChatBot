from langchain.tools import tool
from rag.pipeline import RAGPipeline

rag = RAGPipeline()

@tool
def local_rag_tool(query: str) -> str:
    """
    Use ONLY when the question requires information
    from the user's local laptop documents.
    """
    return rag.run(query)
