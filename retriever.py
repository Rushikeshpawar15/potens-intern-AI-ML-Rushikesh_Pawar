from langchain_community.vectorstores import FAISS
from embedder import embedding

# Load the saved FAISS index
db = FAISS.load_local(
    "vectorstore",
    embedding,
    allow_dangerous_deserialization=True
)

# Create retriever
retriever = db.as_retriever(
    search_kwargs={"k":3}
)