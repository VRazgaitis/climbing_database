import sqlite3

def delete_row(db_name, table_name, column_name, column_value):
    try:
        # Connect to the SQLite database
        conn = sqlite3.connect(db_name)
        cursor = conn.cursor()
        sql_query = f"DELETE FROM {table_name} WHERE {column_name} = ?"
        cursor.execute(sql_query, (column_value,))
        conn.commit()
        print(f"Row where {column_name} = {column_value} deleted successfully.")

    except sqlite3.Error as error:
        print(f"Error while connecting to SQLite: {error}")

    finally:
        # Close the connection
        if conn:
            conn.close()

# Usage example
if __name__ == "__main__":
    db_name = 'Database/MyClimb.db'
    table_name = 'Routes'
    column_name = 'RouteId'
    column_value = 3561  
    delete_row(db_name, table_name, column_name, column_value)
