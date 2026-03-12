from langchain.chains import RetrievalQA
from langchain_openai import AzureChatOpenAI

from backend.pdf_loader import load_pdfs
from backend.vector_store import create_vector_store
from backend.config import *


def create_rag_chain(pdf_paths):

    # Load and split PDFs
    chunks = load_pdfs(pdf_paths)

    # Create vector database
    vectorstore = create_vector_store(chunks)

    # Better retriever settings
    retriever = vectorstore.as_retriever(
        search_type="similarity",
        search_kwargs={"k": 3}
    )

    # Azure OpenAI LLM
    llm = AzureChatOpenAI(
        azure_endpoint=AZURE_OPENAI_ENDPOINT,
        api_key=AZURE_OPENAI_API_KEY,
        api_version=AZURE_OPENAI_API_VERSION,
        deployment_name=AZURE_OPENAI_DEPLOYMENT_NAME,
        temperature=0,
        max_tokens=500
    )

    # Create RAG QA chain
    qa_chain = RetrievalQA.from_chain_type(
        llm=llm,
        retriever=retriever,
        return_source_documents=True
    )

    return qa_chain