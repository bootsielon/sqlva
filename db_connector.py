# db_connector.py

class DatabaseConnector:
    def connect(self):
        raise NotImplementedError("This method should be overridden by subclasses")
    
    def query(self, query: str):
        raise NotImplementedError("This method should be overridden by subclasses")
    
    def get_schema(self):
        raise NotImplementedError("This method should be overridden by subclasses")

# Example implementation for Snowflake (SQL)
class SnowflakeConnector(DatabaseConnector):
    def __init__(self, credentials):
        self.conn = self.connect(credentials)

    def connect(self, credentials):
        import snowflake.connector
        return snowflake.connector.connect(**credentials)

    def query(self, query: str):
        cursor = self.conn.cursor()
        cursor.execute(query)
        return cursor.fetchall()

    def get_schema(self):
        return self.query("SHOW TABLES")  # Example for Snowflake

# Example implementation for MongoDB (NoSQL)
class MongoDBConnector(DatabaseConnector):
    def __init__(self, credentials):
        self.client = self.connect(credentials)

    def connect(self, credentials):
        from pymongo import MongoClient
        return MongoClient(credentials["uri"])

    def query(self, query: dict):
        db = self.client[query["database"]]
        collection = db[query["collection"]]
        return list(collection.find(query["filter"]))

    def get_schema(self):
        # MongoDB does not have a fixed schema, so return collections
        return self.client.list_database_names()
