from rag import ask_question

print("=" * 60)
print("📚 RAG Document Question Answering System")
print("=" * 60)

while True:
    question = input("\nAsk a question (type 'exit' to quit): ")

    if question.lower() == "exit":
        break

    answer, docs = ask_question(question)

    print("\nAnswer:\n")
    print(answer)

    print("\nSources:")
    shown = set()

    for doc in docs:
        source = doc.metadata.get("source", "Unknown")
        page = doc.metadata.get("page", "Unknown")

        if (source, page) not in shown:
            print(f"- {source} | Page {page}")
            shown.add((source, page))