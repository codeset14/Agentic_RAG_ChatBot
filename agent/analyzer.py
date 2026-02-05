from langchain.agents import create_tool_calling_agent, AgentExecutor
from rag.llm import get_llm

from tools.rag_tool import local_rag_tool
from tools.wikipedia_tool import wikipedia_tool
from tools.tavily_tool import tavily_tool

from agent.prompts import ANALYZER_PROMPT

llm = get_llm()

tools = [
    local_rag_tool,
    wikipedia_tool,
    tavily_tool
]

agent = create_tool_calling_agent(
    llm=llm,
    tools=tools,
    prompt=ANALYZER_PROMPT   # ✅ REQUIRED
)

executor = AgentExecutor(
    agent=agent,
    tools=tools,
    verbose=True
)

def analyzer_node(state):
    result = executor.invoke({
        "messages": state["messages"]
    })

    return {
        "messages": state["messages"] + result["messages"]
    }
