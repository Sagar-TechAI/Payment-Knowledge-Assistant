import streamlit as st

with st.sidebar:
    st.header("Project Information")
    st.write()
    st.write()
    st.subheader("Supportted Files")
    st.write("PDF")
    st.write("TXT")
    st.subheader("Developer")
    st.write("Sagar Agarwal")
    st.success("Status: Ready")
st.set_page_config(
    page_title="Payment Knowledge Assistant",
    page_icon="💳",
    layout="wide"
)

st.title("💳 Payment Knowledge Assistant")

st.markdown("AI-powered assistant for understanding payment documents and answering domain-related questions.")

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


