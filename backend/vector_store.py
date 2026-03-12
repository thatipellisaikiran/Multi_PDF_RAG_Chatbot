from pinecone import Pinecone, ServerlessSpec
from langchain_pinecone import PineconeVectorStore
from langchain_openai import AzureOpenAIEmbeddings
from backend.config import *

def create_vector_store(chunks):

    embeddings = AzureOpenAIEmbeddings(
        azure_endpoint=AZURE_OPENAI_ENDPOINT,
        api_key=AZURE_OPENAI_API_KEY,
        api_version=AZURE_OPENAI_API_VERSION,
        azure_deployment=AZURE_OPENAI_EMBEDDING_DEPLOYMENT
    )

    pc = Pinecone(api_key=PINECONE_API_KEY)

    # Create index if it doesn't exist
    if PINECONE_INDEX_NAME not in [i["name"] for i in pc.list_indexes()]:
        pc.create_index(
            name=PINECONE_INDEX_NAME,
            dimension=1536,
            metric="cosine",
            spec=ServerlessSpec(
                cloud="aws",
                region="us-east-1"
            )
        )

    index = pc.Index(PINECONE_INDEX_NAME)

    vectorstore = PineconeVectorStore(
        index=index,
        embedding=embeddings
    )

    vectorstore.add_documents(chunks)

    return vectorstore