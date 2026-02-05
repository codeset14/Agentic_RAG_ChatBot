from langchain_groq import ChatGroq
import os

def get_llm():
    return ChatGroq(
        model="llama3-8b-8192",
        temperature=0,
        api_key=os.getenv("GROQ_API_KEY")
    )
