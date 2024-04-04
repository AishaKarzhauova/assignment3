import pytest
from Assignment3SW import DatabaseConnection



def test_database_connection():
    connection1 = DatabaseConnection.get_instance()
    connection2 = DatabaseConnection.get_instance()
    assert connection1 is connection2
    print("Singleton test passed.")

    if connection1 is connection2:
        connection_info = connection1.get_connection_info()
        print("\nDatabase Connection Information:")
        print("Hostname:", connection_info["hostname"])
        print("Username:", connection_info["username"])
        print("Database Name:", connection_info["database_name"])


