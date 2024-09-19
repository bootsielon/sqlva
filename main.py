# main.py
from app.pinecone_connector import initialize_pinecone
from app.snowflake_connector import initialize_sessions
from app.snowflake_connector import SnowflakeConnector
from app.llm_connector import OpenAIConnector
from app.ui import run_chatbot


def main() -> None:
    # Initialize connectors
    db_connector = SnowflakeConnector(credentials={"user": "your_user", "password": "your_password", "account": "your_account"})
    llm_connector = OpenAIConnector(api_key="your_openai_api_key")

    initialize_pinecone()  # Initialize Pinecone vector store
    run_chatbot(db_connector, llm_connector)  # Run the chatbot


def main_old() -> None:
    conn = initialize_sessions()  # Initialize Snowflake and OpenAI sessions
    initialize_pinecone()  # Initialize Pinecone vector store
    run_chatbot(conn)  # Run the chatbot

if __name__ == "__main__":
    main()
