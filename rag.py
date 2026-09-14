from groq import Groq
from retriever import retriever
import os

SYSTEM_PROMPT = """
You are a helpful AI assistant.

Answer ONLY using the provided context.

If the answer cannot be found in the context, reply exactly:

"I don't know based on the provided documents."

Do not make up information.
"""

client = Groq(api_key=os.getenv("GROQ_API_KEY"))


def ask_question(question):
    # Retrieve relevant chunks
    docs = retriever.invoke(question)

    # Combine retrieved document text
    context = "\n\n".join(
        [doc.page_content for doc in docs]
    )

    prompt = f"""
Context:
{context}

Question:
{question}

Answer:
"""

    response = client.chat.completions.create(
        model="llama-3.1-8b-instant",
        messages=[
            {
                "role": "system",
                "content": SYSTEM_PROMPT
            },
            {
                "role": "user",
                "content": prompt
            }
        ],
        temperature=0
    )

    answer = response.choices[0].message.content

    return answer, docs