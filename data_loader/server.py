import psycopg2

# Connection parameters
connection_params = {
    "user": "postgres",
    "password": "test1234",
    "host": "192.168.225.86",
    "port": "5432",
    "database": "postgres"
}

def connect_db():
    try:
        # Connect to PostgreSQL
        print("Connecting to PostgreSQL ...")
        connection = psycopg2.connect(**connection_params)

        # Create a cursor object
        cursor = connection.cursor()

        # Execute a simple query
        cursor.execute("SELECT now() AS run_at;")
        result = cursor.fetchone()

        # Print the result
        print(f"Run at date-time: {result[0]}")

        # Close the cursor and connection
        cursor.close()
        connection.close()

        print("Execution Completed ...")

    except Exception as e:
        print(f"Error while connecting to the database: {e}")

# Call the function to connect to the database
connect_db()

