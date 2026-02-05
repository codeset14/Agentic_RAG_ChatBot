import streamlit as st
from langchain_core.messages import HumanMessage
from agent.graph import build_graph

st.set_page_config(page_title="Agentic RAG", layout="wide")

st.title("🧠 Agentic RAG Assistant")

# Build graph once
@st.cache_resource
def load_agent():
    return build_graph()

graph = load_agent()

# Chat history (frontend only)
if "chat" not in st.session_state:
    st.session_state.chat = []

# Input box
query = st.chat_input("Ask something...")

# Render previous messages
for msg in st.session_state.chat:
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])

if query:
    # Show user message
    st.session_state.chat.append({"role": "user", "content": query})
    with st.chat_message("user"):
        st.markdown(query)

    # Invoke agent
    with st.chat_message("assistant"):
        with st.spinner("Thinking..."):
            result = graph.invoke({
                "messages": [HumanMessage(content=query)]
            })

            answer = result["messages"][-1].content
            st.markdown(answer)

    st.session_state.chat.append({"role": "assistant", "content": answer})
