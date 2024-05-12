import csv
import sqlite3

def process_csv_routes(path):
    with sqlite3.connect('MyClimb.db') as conn:

        cursor = conn.cursor()

        insert_query = '''
        INSERT INTO Routes (RouteName, Location, URL, AVG_STARS, RouteType, Rating)
        VALUES (?, ?, ?, ?, ?, ?);
        '''

        with open(path, 'r') as file:
            routeDictionary = csv.DictReader(file)
            for row in routeDictionary:
                cursor.execute(insert_query, 
                               (int(row['RouteName']), 
                                row['Location'], 
                                row['URL'], 
                                float(row['AVG_STARS']), 
                                row['RouteType'], 
                                row['Difficulty_Rating']))

process_csv_routes('Data/routes.csv')