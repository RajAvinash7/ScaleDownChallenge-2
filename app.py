import streamlit as st
from rag import ask

st.set_page_config(page_title="University FAQ Assistant")

st.title("🎓 University FAQ Assistant")

question = st.text_input("Ask a question")

if question:
    answer, refs = ask(question)

    st.subheader("Answer")
    st.write(answer)

    st.subheader("Sources")
    for r in refs:
        st.write("-", r)
