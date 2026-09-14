from retriever import retriever

query = input("Enter your question: ")

docs = retriever.invoke(query)

print("\nRetrieved Documents:\n")

for i, doc in enumerate(docs, start=1):
    print("=" * 50)
    print(f"Chunk {i}")
    print("Source:", doc.metadata.get("source"))
    print("Page:", doc.metadata.get("page"))
    print(doc.page_content[:500])