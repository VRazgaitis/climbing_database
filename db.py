import csv
import sqlite3

def create_my_climb(file_path, db_path='Database/MyClimb.db'):
    with sqlite3.connect(db_path) as conn:
        with open(file_path, 'r') as create_tables:
            create_climb_tables = create_tables.read()
        conn.executescript(create_climb_tables)
        conn.commit()

create_my_climb('Database/schema.sql')