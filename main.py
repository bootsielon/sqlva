from app.snowflake_connector import initialize_sessions
from app.ui import run_chatbot
from app.pinecone_connector import initialize_pinecone

def main() -> None:
    conn = initialize_sessions()  # Initialize Snowflake and OpenAI sessions
    initialize_pinecone()  # Initialize Pinecone vector store
    run_chatbot(conn)  # Run the chatbot

if __name__ == "__main__":
    main()
