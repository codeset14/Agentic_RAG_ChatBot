from dotenv import load_dotenv
load_dotenv()

from langchain.tools import tool
from langchain_community.utilities import WikipediaAPIWrapper

wiki = WikipediaAPIWrapper(
    top_k_results=3,
    doc_content_chars_max=3000
)

@tool
def wikipedia_tool(query: str) -> str:
    """
    Use this tool for general knowledge, definitions,
    history, or conceptual explanations.
    """
    return wiki.run(query)
