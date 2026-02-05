from rag.llm import get_llm
from langchain_core.messages import AIMessage

llm = get_llm()

GENERATOR_PROMPT = """
You are the final answer generator.

Your task:
- Produce a clear, concise, and helpful answer for the user.
- Use information from previous messages and tool outputs if present.
- Do NOT mention tools, agents, or internal reasoning.
- Answer directly to the user.
"""

def generator_node(state):
    """
    LangGraph node responsible for generating the final response.
    """
    # Use full conversation context
    messages = state["messages"]

    # Call LLM with system instruction + conversation
    response = llm.invoke(
        GENERATOR_PROMPT + "\n\nUser request:\n" + messages[-1].content
    )

    return {
        "messages": messages + [
            AIMessage(content=response.content)
        ]
    }
