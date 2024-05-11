import csv
import sqlite3

def create_my_climb(file_path, db_path='Database/MyClimb.db'):
    with sqlite3.connect(db_path) as conn:
        with open(file_path, 'r') as sql_hotel:
            hotel_script = sql_hotel.read()
        conn.executescript(hotel_script)
        conn.commit()

create_my_climb('Database/MyClimb.sql')