from rag.pipeline import RAGPipeline

rag = RAGPipeline()

query = "What is Data Science?"
answer = rag.run(query)

print("\n🧠 ANSWER:\n")
print(answer)
