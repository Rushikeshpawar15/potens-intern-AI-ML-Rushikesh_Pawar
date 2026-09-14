from loader import load_documents
from chunker import chunk_documents
from embedder import embedding

from langchain_community.vectorstores import FAISS

# Load all documents
documents = load_documents("data")

print(f"Loaded {len(documents)} pages.")

# Split into chunks
chunks = chunk_documents(documents)

print(f"Created {len(chunks)} chunks.")

# Create FAISS index
db = FAISS.from_documents(chunks, embedding)

# Save index
db.save_local("vectorstore")

print("FAISS index created successfully!")