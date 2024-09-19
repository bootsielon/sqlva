# chat_handler.py
import streamlit as st
from app.rag_retrieval import run_rag_workflow
from app.sql_generator import generate_query
from app.query_generator import QueryGenerator
import re


def handle_user_input(db_connector, llm_connector):
    if st.session_state.messages and st.session_state.messages[-1]["role"] != "assistant":
        user_input = st.session_state.messages[-1]["content"]

        # Initialize QueryGenerator
        query_generator = QueryGenerator(db_connector, llm_connector)

        # Use RAG for retrieval-augmented responses
        rag_response = run_rag_workflow(user_input, llm_connector)
        
        # Fallback to query generation if no relevant documents are retrieved
        if not rag_response:
            response_content = query_generator.generate_query(user_input)
        else:
            response_content = rag_response

        st.session_state.messages.append({"role": "assistant", "content": response_content})

        # Extract and run query if present
        sql_match = re.search(r"```sql\n(.*)\n```", response_content, re.DOTALL)
        if sql_match:
            query = sql_match.group(1).strip()
            results = query_generator.run_query(query)
            st.dataframe(results)



def handle_user_input_plain(conn, table_definitions):
    if st.session_state.messages and st.session_state.messages[-1]["role"] != "assistant":
        user_input = st.session_state.messages[-1]["content"]

        # Use RAG for retrieval-augmented responses
        rag_response = run_rag_workflow(user_input)
        
        # Fallback to SQL generation if no useful data is retrieved
        if not rag_response:
            response_content = generate_query(user_input, table_definitions)
        else:
            response_content = rag_response

        st.session_state.messages.append({"role": "assistant", "content": response_content})

        # Extract and run SQL if present
        sql_match = re.search(r"```sql\n(.*)\n```", response_content, re.DOTALL)
        if sql_match:
            sql = sql_match.group(1).strip()
            if sql.upper().startswith("SELECT"):
                try:
                    message["results"] = conn.query(sql)
                    st.dataframe(message["results"])
                except Exception as e:
                    st.write(f"Error executing query: {e}")
