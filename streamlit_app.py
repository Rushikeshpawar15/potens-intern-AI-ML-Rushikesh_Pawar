import streamlit as st
from rag import ask_question

st.set_page_config(page_title="RAG Chatbot", page_icon="")

st.title("AI Chatbot")

question = st.text_input("Ask your question")

if st.button("Ask"):

    if question.strip():

        with st.spinner("Thinking..."):

            answer, docs = ask_question(question)

        st.subheader("Answer")
        st.write(answer)

        st.subheader("Retrieved Sources")

        for doc in docs:
            with st.expander(
                f"{doc.metadata.get('source')} | Page {doc.metadata.get('page')}"
            ):
                st.write(doc.page_content)

    else:
        st.warning("Please enter a question.")