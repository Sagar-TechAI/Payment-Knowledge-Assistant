import streamlit as st

st.set_page_config(
    page_title="Payment Knowledge Assistant",
    page_icon="💳",
    layout="wide"
)

st.title("💳 Payment Knowledge Assistant")

st.markdown("### Project SagarVerse 🚀")

uploaded_file = st.file_uploader(
    "Upload Payment Document",
    type=["pdf","txt"]
)

question = st.text_input(
    "Ask a payment related question:"
)

if st.button("Submit"):
    st.success(f"Question received: {question}")

if uploaded_file:
    st.success(
        f"File Uploaded: {uploaded_file.name}"
    )