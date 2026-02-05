from dotenv import load_dotenv
load_dotenv()

from langchain_community.tools.tavily_search import TavilySearchResults

# OFFICIAL LangChain Tavily tool (Runnable)
tavily_tool = TavilySearchResults(max_results=5)
