import sqlite3

# Step 2: Connect to the SQLite database
# If the database does not exist, it will be created
conn = sqlite3.connect('example.db')

# Step 3: Create a cursor object
cur = conn.cursor()

# Step 4: Execute the SELECT query
cur.execute('SELECT * FROM table_name')

# Step 5: Fetch the results
rows = cur.fetchall()

# Print the results
for row in rows:
    print(row)

# Step 6: Close the connection
conn.close()
