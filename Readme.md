/sqlva (virtual-assistant)
│
├── /app
│   ├── __init__.py
│   ├── main.py                  # Entry point for Streamlit app
│   ├── ui.py                    # Handles UI elements, displays messages, and inputs
│   ├── chat_handler.py           # Handles user input, chat session state, OpenAI, and Pinecone interactions
│   ├── sql_generator.py          # Contains the function that generates SQL queries using OpenAI
│   ├── snowflake_connector.py    # Contains functions for connecting and interacting with Snowflake
│   ├── rag_retrieval.py          # Handles Pinecone and LangChain RAG logic
│   └── pinecone_connector.py     # Handles Pinecone connection and vector store logic
│
├── /utils
│   ├── __init__.py
│   └── helpers.py                # Contains helper functions like get_table_definitions, maintain_state
│
├── requirements.txt              # List of dependencies (pip install -r requirements.txt)
└── config.toml                   # Configuration file for managing secrets (API keys, Pinecone API, Snowflake credentials)
