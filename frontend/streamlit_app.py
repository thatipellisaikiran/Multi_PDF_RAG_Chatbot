import streamlit as st
import requests

# FastAPI URL
API_URL = "http://127.0.0.1:8000"

st.set_page_config(page_title="Multi PDF RAG Bot")

st.title("📄 Multi PDF RAG Chatbot")

st.write("Upload PDFs and ask questions from them.")

# Upload PDFs
uploaded_files = st.file_uploader(
    "Upload PDF files",
    type="pdf",
    accept_multiple_files=True
)

# Upload Button
if uploaded_files:

    if st.button("Upload PDFs to Server"):

        files = []

        for file in uploaded_files:
            files.append(
                ("files", (file.name, file.getvalue(), "application/pdf"))
            )

        try:

            response = requests.post(
                f"{API_URL}/upload",
                files=files
            )

            if response.status_code == 200:
                data = response.json()
                st.success(data["message"])

            else:
                st.error("Upload failed")
                st.text(response.text)

        except Exception as e:
            st.error("Could not connect to FastAPI server")
            st.text(str(e))


st.divider()

# Ask Question Section
st.subheader("Ask a Question")

question = st.text_input("Enter your question")

if st.button("Ask Question"):

    if question == "":
        st.warning("Please enter a question")

    else:

        try:

            response = requests.get(
                f"{API_URL}/ask",
                params={"question": question}
            )

            if response.status_code == 200:

                data = response.json()

                st.success("Answer")
                st.write(data["answer"])

            else:

                st.error("API Error")
                st.text(response.text)

        except Exception as e:

            st.error("FastAPI server not reachable")
            st.text(str(e))