import pinecone
import os
from langchain.vectorstores import Pinecone
from langchain.embeddings.openai import OpenAIEmbeddings

# Initialize Pinecone and LangChain vector store
def initialize_pinecone() -> Pinecone:
    pinecone_api_key = os.getenv("PINECONE_API_KEY")
    pinecone.init(api_key=pinecone_api_key, environment="us-west1-gcp")

    # Create Pinecone Index
    index_name = "snowflake-index"
    if index_name not in pinecone.list_indexes():
        pinecone.create_index(index_name, dimension=1536)  # Adjust based on embedding size

    # Initialize OpenAI Embeddings
    embeddings = OpenAIEmbeddings()

    # Connect Pinecone to LangChain Vector Store
    pinecone_index = pinecone.Index(index_name)
    vector_store = Pinecone(pinecone_index, embeddings.embed_query, "text")
    return vector_store
