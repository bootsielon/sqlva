def get_table_definitions(conn):
    data = get_databases_schemas_tables(conn)
    markdown = [f'### {row["TABLE_CATALOG"]}.{row["TABLE_SCHEMA"]}.{row["TABLE_NAME"]}' for _, row in data.iterrows()]
    return '\n'.join(markdown)

def maintain_state(state):
    for k, v in state.items():
        state[k] = v
