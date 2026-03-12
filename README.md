# Multi-PDF RAG Chatbot (Generative AI Project)

## 🚀 Overview

This project is an AI-powered chatbot that can answer questions from
multiple PDF documents using **Retrieval-Augmented Generation (RAG)**.
Users can upload PDF files and ask questions, and the system retrieves
relevant content from the documents and generates accurate answers.

## 🧠 Architecture

1.  Upload PDF files
2.  Split text into smaller chunks
3.  Generate embeddings using Azure OpenAI
4.  Store embeddings in Pinecone vector database
5.  Retrieve relevant chunks based on user query
6.  Generate final answer using GPT model

## 🛠 Tech Stack

-   Python
-   FastAPI (Backend API)
-   Streamlit (Frontend UI)
-   LangChain
-   Azure OpenAI (LLM + Embeddings)
-   Pinecone (Vector Database)
-   SQLite (Chat history storage)

## 📂 Project Structure

    multipdf-rag-bot
    │
    ├── backend
    │   ├── app.py
    │   ├── rag_chain.py
    │   ├── vector_store.py
    │   ├── pdf_loader.py
    │   ├── config.py
    │   └── database.py
    │
    ├── frontend
    │   └── streamlit_app.py
    │
    ├── data
    │   └── chat.db
    │
    ├── .env
    ├── requirements.txt
    └── README.md

## ⚙️ Installation

### 1️⃣ Clone the repository

    git clone https://github.com/yourusername/multipdf-rag-chatbot.git
    cd multipdf-rag-chatbot

### 2️⃣ Install dependencies

    pip install -r requirements.txt

### 3️⃣ Create `.env` file

Add the following environment variables:

    AZURE_OPENAI_API_KEY=your_api_key
    AZURE_OPENAI_ENDPOINT=your_endpoint
    AZURE_OPENAI_DEPLOYMENT_NAME=gpt-4o
    AZURE_OPENAI_EMBEDDING_DEPLOYMENT=text-embedding-3-small

    PINECONE_API_KEY=your_pinecone_key
    PINECONE_INDEX_NAME=rag-bot

## ▶️ Run the Application

### Start FastAPI backend

    uvicorn backend.app:app --reload

### Start Streamlit frontend

    streamlit run frontend/streamlit_app.py

## 💡 Features

-   Upload and analyze multiple PDFs
-   Semantic search using vector embeddings
-   Retrieval-Augmented Generation (RAG)
-   AI-generated answers from document context
-   Chat history storage

## 📸 Demo

Upload a PDF → Ask a question → Get an AI-generated answer based on
document content.

## 🔮 Future Improvements

-   Add conversational memory
-   Improve retrieval accuracy
-   Deploy on cloud platforms
-   Add authentication
