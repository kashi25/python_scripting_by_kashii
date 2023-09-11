import psycopg2

# Database connection parameters
hostname = "localhost"
database_name = "scr"
username = "postgres"
password = "djangohero"
port = 5432

# Function to establish a database connection
def create_connection():
    try:
        connection = psycopg2.connect(
            host=hostname,
            database=database_name,
            user=username,
            password=password,
            port=port
        )
        return connection
    except Exception as e:
        print(f"Error: {e}")
        return None

# Function to execute a SQL query with parameters
def execute_query(connection, query, params=None):
    try:
        cursor = connection.cursor()
        if params:
            cursor.execute(query, params)
        else:
            cursor.execute(query)
        connection.commit()
        print("Query executed successfully")
    except Exception as e:
        print(f"Error executing query: {e}")

# Create a connection
connection = create_connection()

if connection:
    try:
        # Example: Insert data into a table
        insert_query = "INSERT INTO your_table_name (column1, column2) VALUES (%s, %s)"
        data_to_insert = ('value1', 'value2')
        execute_query(connection, insert_query, data_to_insert)
    except Exception as e:
        print(f"Error: {e}")

    # Example: Select data from a table
    # select_query = "SELECT * FROM your_table_name"
    # execute_query(connection, select_query)

    # Example: Update data in a table
    # update_query = "UPDATE your_table_name SET column1 = 'new_value' WHERE column2 = 'value2'"
    # execute_query(connection, update_query)

    # Example: Delete data from a table
    # delete_query = "DELETE FROM your_table_name WHERE column2 = 'value2'"
    # execute_query(connection, delete_query)

    # Close the database connection
    connection.close()
else:
    print("Failed to connect to the database")
