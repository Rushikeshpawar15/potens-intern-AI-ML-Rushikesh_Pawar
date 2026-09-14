# 📄 RAG Document Question Answering System

A Retrieval-Augmented Generation (RAG) application built using **Flask**, **LangChain**, **ChromaDB**, **Sentence Transformers**, **Groq Llama 3.3**, and **Streamlit**.

The application allows users to upload and index documents, ask natural language questions, receive answers with citations, compare two documents for contradictions, and supports multilingual queries.

---

# Features

*  Document ingestion (PDF, DOCX, TXT)
*  Intelligent document chunking
* Vector embeddings using Sentence Transformers
* Semantic search using ChromaDB
* Answer generation using Groq Llama 3.3
* Answers with citations
* Multilingual query support
* Hallucination prevention
* Document contradiction detection
* Streamlit web interface
* Flask REST API

---

# Project Structure

```text
Q1_RAG_PROJECT/
│
├── app.py
├── build_index.py
├── chunker.py
├── embedder.py
├── loader.py
├── prompt.py
├── rag.py
├── retriever.py
├── streamlit_app.py
├── test_retriever.py
│
├── data/
│   └── (Place your PDF/DOCX/TXT files here)
│
├── vectorstore/
│
├── .env
├── requirements.txt
└── README.md
```

---

# Tech Stack

* Python 3.11+
* Flask
* Streamlit
* LangChain
* ChromaDB
* Sentence Transformers
* HuggingFace Embeddings
* Groq API (Llama 3.3)
* PyPDF
* python-docx

---

# Installation

## 1. Clone the repository

```bash
git clone <repository-url>
cd Q1_RAG_PROJECT
```

---

## 2. Create Virtual Environment

### Windows

```bash
python -m venv venv
```

Activate:

```bash
venv\Scripts\activate
```

### Linux / macOS

```bash
python3 -m venv venv
source venv/bin/activate
```

---

## 3. Install Dependencies

```bash
pip install -r requirements.txt
```

---

## 4. Configure Environment Variables

Create a `.env` file in the project root.

Example:

```text
GROQ_API_KEY=YOUR_GROQ_API_KEY
```

---

# Adding Documents

Place all supported documents inside the `data/` folder.

Example:

```text
data/
│
├── HRPolicy.pdf
├── EmployeeHandbook.pdf
├── LeavePolicy.pdf
├── ResearchPaper.pdf
└── CompanyGuide.pdf
```

Supported file types:

* PDF
* DOCX
* TXT

---

# Build the Vector Database

After adding documents, generate embeddings by running:

```bash
python build_index.py
```

This process:

* Reads all documents
* Splits documents into chunks
* Generates embeddings
* Stores vectors in ChromaDB

---

# Run the Flask Backend

Start the API server:

```bash
python app.py
```

The backend starts on:

```text
http://localhost:5000
```

---

# Run the Streamlit Frontend

Open a new terminal.

Activate the virtual environment again.

Run:

```bash
streamlit run streamlit_app.py
```

or

```bash
python -m streamlit run streamlit_app.py
```

The application opens at:

```text
http://localhost:8501
```

---

# Using the Application

## Ask Questions

Examples:

* What is the leave policy?
* What are the working hours?
* Explain the reimbursement policy.
* कंपनी की छुट्टी नीति क्या है?
* कंपनीचे रजा धोरण काय आहे?

The application retrieves relevant document chunks, generates an answer, and displays citations.

---

## Contradiction Detection

Use the contradiction endpoint (or UI if implemented) to compare two indexed documents.

Example:

* HRPolicy.pdf
* RemoteWorkPolicy.pdf

The application reports whether the documents contain conflicting information and explains the reason.

---

# Updating Documents

Whenever a new document is added to the `data/` folder:

1. Add the file.
2. Run:

```bash
python build_index.py
```

3. Restart the Flask backend if it is running.

The new document is then available for querying.

---

# API Endpoints

## Home

```
GET /
```

---

## Ask Question

```
POST /ask
```

Example request:

```json
{
  "question": "What is the leave policy?"
}
```

---

## Check Contradiction

```
POST /contradict
```

Example request:

```json
{
  "doc1": "HRPolicy.pdf",
  "doc2": "RemoteWorkPolicy.pdf"
}
```

---

# Hallucination Prevention

The application only answers using the indexed documents.

If the answer is not available, it responds with:

> "The uploaded documents do not contain enough information to answer this question."

---

# Citation Format

Each response includes:

* Source document
* Page number (if available)
* Chunk number
* Relevant text snippet

---

# Future Improvements

* Drag-and-drop document upload
* Automatic indexing after upload
* Support for additional document formats
* Authentication
* Docker deployment
* Conversation history
* Hybrid keyword + semantic search
* Re-ranking for improved retrieval accuracy

---

# License

This project is intended for educational purposes and assignment submission.
