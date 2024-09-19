# query_generator.py

from app.llm_connector import LLMConnector
from app.db_connector import DatabaseConnector

class QueryGenerator:
    def __init__(self, db_connector: DatabaseConnector, llm_connector: LLMConnector):
        self.db_connector = db_connector
        self.llm_connector = llm_connector

    def generate_query(self, user_input: str):
        schema = self.db_connector.get_schema()
        prompt = f"The following is the schema: {schema}. {user_input}"
        
        # Use the LLM to generate a query based on the schema
        generated_query = self.llm_connector.generate_response(prompt)
        return generated_query

    def run_query(self, query: str):
        return self.db_connector.query(query)
