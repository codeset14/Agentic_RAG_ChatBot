from langgraph.graph import StateGraph, END
from agent.state import AgentState
from agent.supervisor import supervisor_node
from agent.analyzer import analyzer_node
from agent.generator import generator_node

def build_graph():
    graph = StateGraph(AgentState)

    graph.add_node("supervisor", supervisor_node)
    graph.add_node("analyzer", analyzer_node)
    graph.add_node("generator", generator_node)

    graph.set_entry_point("supervisor")

    graph.add_conditional_edges(
        "supervisor",
        lambda state: state["decision"],
        {
            "analyze": "analyzer",
            "direct": "generator"
        }
    )

    graph.add_edge("analyzer", "generator")
    graph.add_edge("generator", END)

    return graph.compile()
