from langchain.prompts import PromptTemplate

PROMPT = PromptTemplate(
    input_variables=["context", "question"],
    template="""
You are a helpful AI assistant.

Answer ONLY using the provided context.

If the answer cannot be found in the context, reply exactly:

"I don't know based on the provided documents."

Do not make up information.

Context:
{context}

Question:
{question}

Answer:
"""
)