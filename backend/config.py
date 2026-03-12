

import os
from dotenv import load_dotenv

load_dotenv()

# ===============================
# Azure OpenAI Configuration
# ===============================

AZURE_OPENAI_API_KEY = os.getenv("AZURE_OPENAI_API_KEY")

AZURE_OPENAI_ENDPOINT = os.getenv("AZURE_OPENAI_ENDPOINT")

AZURE_OPENAI_EMBEDDING_DEPLOYMENT = os.getenv("AZURE_OPENAI_EMBEDDING_DEPLOYMENT")

AZURE_OPENAI_API_VERSION = os.getenv("AZURE_OPENAI_API_VERSION")

AZURE_OPENAI_DEPLOYMENT_NAME = os.getenv("AZURE_OPENAI_DEPLOYMENT_NAME")


# ===============================
# Pinecone Configuration
# ===============================

PINECONE_API_KEY = os.getenv("PINECONE_API_KEY")

# Vector database name
PINECONE_INDEX_NAME = "rag-bot"