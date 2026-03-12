from langchain.chains import RetrievalQA
from langchain_openai import AzureChatOpenAI
from pdf_loader import load_pdfs
from vector_store import init_vectorstore
from config import *

def create_rag_chain(pdf_paths):

    # Load and split PDFs
    chunks = load_pdfs(pdf_paths)

    # Create vector database
    vectorstore = init_vectorstore(chunks)

    retriever = vectorstore.as_retriever()

    # Azure OpenAI LLM
    llm = AzureChatOpenAI(
        azure_endpoint=AZURE_OPENAI_ENDPOINT,
        api_key=AZURE_OPENAI_API_KEY,
        api_version=AZURE_OPENAI_API_VERSION,
        deployment_name=AZURE_OPENAI_DEPLOYMENT_NAME,
        temperature=0
    )

    # Create RAG QA chain
    qa_chain = RetrievalQA.from_chain_type(
        llm=llm,
        retriever=retriever,
        return_source_documents=True
    )

    return qa_chain