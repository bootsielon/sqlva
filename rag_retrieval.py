from langchain.chains import RetrievalQA
from langchain.llms import OpenAI
from app.pinecone_connector import initialize_pinecone

# Function to run RAG workflow with LangChain
def run_rag_workflow(query: str) -> str:
    # Initialize Pinecone vector store
    vector_store = initialize_pinecone()

    # Initialize the LLM (OpenAI GPT)
    llm = OpenAI(model_name="gpt-3.5-turbo")

    # Build the RetrievalQA chain
    qa_chain = RetrievalQA(llm=llm, retriever=vector_store.as_retriever())

    # Get the response from the chain by retrieving relevant docs and augmenting the answer
    response = qa_chain.run(query)
    return response
