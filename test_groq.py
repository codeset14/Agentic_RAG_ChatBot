from rag.llm import get_llm

llm = get_llm()
print(llm.invoke("Say hello in one sentence"))
