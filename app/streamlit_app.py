import streamlit as st
import requests

BACKEND_URL = "http://localhost:8000"

st.set_page_config(page_title="AI Research Assistant", layout="centered")
st.title("AI Research Assistant")

# upload pdf
st.subheader("Upload a research paper")
uploaded_file = st.file_uploader("Choose a PDF file", type=["pdf"])

if uploaded_file is not None:
    with st.spinner("Processing PDF..."):
        files = {"file": uploaded_file}
        response = requests.post(f"{BACKEND_URL}/upload-pdf", files=files)
        if response.status_code == 200 and response.json().get("status") == "success":
            st.success("PDF processed successfully")
        else:
            st.error("Failed to process PDF")


# Ask a question
st.subheader("Ask a question about the uploaded paper")

question = st.text_input("What would you like to know?")
if st.button("Ask"):
    if not question.strip():
        st.warning("Please Enter a question first")
    else:
        with st.spinner("Thinking..."):
            response = requests.post(f"{BACKEND_URL}/ask", data={"question": question})
            if response.status_code == 200:
                answer = response.json().get("answer", "No answer available")
                sources = response.json().get("sources", [])
                st.success("Answer:")
                st.markdown({answer})
                with st.expander("Sources"):
                    for i, (chunk, score) in enumerate(sources):
                        st.markdown(f"**Source {i+1}**")
                        st.code(chunk[:500] + ("..." if len(chunk) > 500 else ""))

            else:
                st.error(f"Failed to get an answer: {response.text}")