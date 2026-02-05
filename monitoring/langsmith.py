from langchain.callbacks.tracers import LangChainTracer

def get_tracer():
    return LangChainTracer(project_name="agentic-laptop-ai")
