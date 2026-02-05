from langchain_core.messages import HumanMessage
from agent.graph import build_graph

graph = build_graph()

# 1️⃣ Should answer directly (NO tools)
print(
    graph.invoke({
        "messages": [HumanMessage(content="What is attention mechanism?")]
    })["messages"][-1].content
)

# 2️⃣ Should use Wikipedia
print(
    graph.invoke({
        "messages": [HumanMessage(content="Explain transformers in simple terms")]
})["messages"][-1].content
)

# 3️⃣ Should use RAG
print(
    graph.invoke({
        "messages": [HumanMessage(content="Summarize my internship project from my laptop files")]
    })["messages"][-1].content
)

# 4️⃣ Should use Tavily
print(
    graph.invoke({
        "messages": [HumanMessage(content="Latest LangGraph updates")]
    })["messages"][-1].content
)
