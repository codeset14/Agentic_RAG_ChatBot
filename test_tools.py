from dotenv import load_dotenv
load_dotenv()

from tools.wikipedia_tool import wikipedia_tool
from tools.tavily_tool import tavily_tool

print("WIKI TEST:")
print(wikipedia_tool.invoke("Attention mechanism in transformers"))

print("\nTAVILY TEST:")
print(tavily_tool.invoke("Latest LangGraph updates"))
