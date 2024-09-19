/sqlva (virtual-assistant)
│
├── /app
│   ├── __init__.py
│   ├── main.py                   # Entry point for Streamlit app
│   ├── ui.py                     # Handles UI elements, displays messages, and inputs
│   ├── chat_handler.py            # Handles user input, chat session state, DB/LLM interactions
│   ├── query_generator.py         # Abstraction layer for generating queries across different DBs
│   ├── db_connector.py            # Abstracted interface for database connections (agnostic to DB type)
│   ├── llm_connector.py           # Abstracted interface for LLM models (agnostic to LLM provider)
│   ├── pinecone_connector.py      # Handles Pinecone connection and vector store logic
│   ├── rag_retrieval.py           # Handles Pinecone and LangChain RAG logic
│
├── /utils
│   ├── __init__.py
│   └── helpers.py                 # Contains helper functions like get_table_definitions, maintain_state
│
├── /config
│   └── config.toml                # Configuration file for managing secrets (API keys, DB credentials)
├── requirements.txt               # List of dependencies (pip install -r requirements.txt)
└── README.md                      # Project documentation
