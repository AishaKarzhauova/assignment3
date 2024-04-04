import json
import threading


class DatabaseConnection:
    _instance = None
    _lock = threading.Lock()

    def __init__(self):
        # load database connection information from configuration file
        self._load_config()

    @staticmethod
    def get_instance():
        if DatabaseConnection._instance is None:
            with DatabaseConnection._lock:
                if DatabaseConnection._instance is None:
                    DatabaseConnection._instance = DatabaseConnection()
        return DatabaseConnection._instance

    def _load_config(self):
        # load configuration from a JSON file
        config_file_path = "database.json"
        with open(config_file_path) as f:
            config = json.load(f)
            self.hostname = config.get("hostname")
            self.username = config.get("username")
            self.password = config.get("password")
            self.database_name = config.get("database_name")

    def execute_query(self, sql_query):
        # method to execute SQL queries
        pass

    def retrieve_results(self):
        # method to retrieve query results
        pass

    def get_connection_info(self):
        # database connection information
        return {
            "hostname": self.hostname,
            "username": self.username,
            "database_name": self.database_name
        }
