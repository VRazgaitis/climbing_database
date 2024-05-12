import csv
import sqlite3

def process_csv_routes(path):
    with sqlite3.connect('Database/MyClimb.db') as conn:

        cursor = conn.cursor()

        insert_query = '''
        INSERT INTO Routes (RouteName, Location, URL, AVG_STARS, RouteType, Difficulty_Rating, Latitude, Longitude)
        VALUES (?, ?, ?, ?, ?, ?, ?, ?);
        '''

        with open(path, 'r') as file:
            routeDictionary = csv.DictReader(file)
            for row in routeDictionary:
                cursor.execute(insert_query, 
                                (row['Route'], 
                                row['Location'], 
                                row['URL'], 
                                float(row['Avg Stars']), 
                                row['Route Type'], 
                                row['Rating'].split()[0],
                                float(row['Area Latitude']),
                                float(row['Area Longitude'])))  # clean out extra chars for danger tags

process_csv_routes('Data/kentucky_routes.csv')