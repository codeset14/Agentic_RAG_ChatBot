from rag.llm import get_llm
from langchain_core.messages import AIMessage

llm = get_llm()

SUPERVISOR_PROMPT = """
You are a supervisor agent.

Your job is to decide how the user query should be handled.

Respond with ONLY ONE WORD:
- analyze  → if the question may need tools, retrieval, or reasoning
- direct   → if you can answer confidently without tools
"""

def supervisor_node(state):
    # Last user message
    user_message = state["messages"][-1].content

    # Ask the LLM to decide
    response = llm.invoke(
        SUPERVISOR_PROMPT + "\n\nUser query:\n" + user_message
    )

    decision = response.content.strip().lower()

    # Safety fallback
    if decision not in ("analyze", "direct"):
        decision = "analyze"

    return {
        "messages": state["messages"],
        "decision": decision
    }
