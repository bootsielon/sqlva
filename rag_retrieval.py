# rag_retrieval.py
from langchain.chains import RetrievalQA
from langchain.llms import OpenAI
from app.pinecone_connector import initialize_pinecone
from app.llm_connector import LLMConnector

# Function to run RAG workflow with LangChain
def run_rag_workflow_plain(query: str) -> str:
    # Initialize Pinecone vector store
    vector_store = initialize_pinecone()

    # Initialize the LLM (OpenAI GPT)
    llm = OpenAI(model_name="gpt-3.5-turbo")

    # Build the RetrievalQA chain
    qa_chain = RetrievalQA(llm=llm, retriever=vector_store.as_retriever())

    # Get the response from the chain by retrieving relevant docs and augmenting the answer
    response = qa_chain.run(query)
    return response



def run_rag_workflow(query: str, llm_connector: LLMConnector) -> str:
    # Initialize Pinecone vector store
    vector_store = initialize_pinecone()

    # Build the RetrievalQA chain using the provided LLM connector
    qa_chain = RetrievalQA(
        retriever=vector_store.as_retriever(),
        llm=llm_connector.generate_response  # Use the LLM-agnostic method
    )

    # Get the response from the chain by retrieving relevant docs and augmenting the answer
    response = qa_chain.run(query)
    return response
