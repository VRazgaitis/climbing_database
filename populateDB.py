import csv
import sqlite3
from util import data_helpers

def process_csv_routes(path):
    """
    Processes route entries into the DB
    """
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
                                row['Rating'].split()[0], # clean out extra chars for danger tags
                                float(row['Area Latitude']),
                                float(row['Area Longitude'])))  
                
def process_csv_climbers(path):
    """
    Processes climbers into the DB
    """
    with sqlite3.connect('Database/MyClimb.db') as conn:
        cursor = conn.cursor()
        insert_query = '''
        INSERT INTO Climbers (ClimberName, DOB)
        VALUES (?, ?);
        '''
        with open(path, 'r') as file:
            climberDictionary = csv.DictReader(file)
            for row in climberDictionary:
                cursor.execute(insert_query, 
                                (row['Name'], row['DOB']))  
                
def process_csv_route_developers(path):
    """
    Processes route developers into the DB
    """
    with sqlite3.connect('Database/MyClimb.db') as conn:
        cursor = conn.cursor()
        insert_query = '''
        INSERT INTO Developed_Routes (DeveloperName, RouteName, DateDeveloped)
        VALUES (?, ?, ?);
        '''
        with open(path, 'r') as file:
            developerDictionary = csv.DictReader(file)
            for row in developerDictionary:
                cursor.execute(insert_query, 
                                (row['Setter Name'], row['Route Name'], row['Date Climbed']))  
                
def process_csv_gear(path):
    """
    Processes climbing gear into the DB
    """
    with sqlite3.connect('Database/MyClimb.db') as conn:
        cursor = conn.cursor()
        insert_query = '''
        INSERT INTO Climbing_equipment (ProductName, Brand, Weight, URL)
        VALUES (?, ?, ?, ?);
        '''
        with open(path, 'r') as file:
            gearDictionary = csv.DictReader(file)
            for row in gearDictionary:
                cursor.execute(insert_query, 
                                (row['Product Name'], row['Brand'], row['Weight (oz)'], row['URL']))  
                
def process_csv_eq_used(path):
    """
    Processes equipment used into the DB
    """
    with sqlite3.connect('Database/MyClimb.db') as conn:
        cursor = conn.cursor()
        insert_query = '''
        INSERT INTO Equipment_used (ProductName, RouteName)
        VALUES (?, ?);
        '''
        with open(path, 'r') as file:
            gearDictionary = csv.DictReader(file)
            for row in gearDictionary:
                cursor.execute(insert_query, 
                                (row['Gear'], row['Route']))  
                
def process_csv_ticklist(climber_name, path):
    """
    Processes individual climbers' ticklists into the DB
    """
    with sqlite3.connect('Database/MyClimb.db') as conn:
        cursor = conn.cursor()
        insert_query = '''
        INSERT INTO Ticks (ClimberName, RouteName, ClimbDate, ClimbStars, AscentStyle, LeadStyle, AscentNotes)
        VALUES (?, ?, ?, ?, ?, ?, ?);
        '''
        with open(path, 'r') as file:
            tickDictionary = csv.DictReader(file)
            for row in tickDictionary:
                cursor.execute(insert_query, 
                                (climber_name, 
                                 row['Route'], 
                                 row['Date'], 
                                 row['Your Stars'], 
                                 row['Style'], 
                                 row['Lead Style'], 
                                 row['Notes']))  

def write_routes():
    """
    Writes all routes contained in Data/Routes into the DB
    """
    route_lists = data_helpers.list_filenames('Data/routes')
    for climbing_location in route_lists:
        print(climbing_location)
        process_csv_routes('Data/Routes/'+climbing_location)

def write_ticks():
    """
    Writes all ticks contained in Data/Routes into the DB
    """
    ticklists = data_helpers.list_filenames('Data/ticklists')
    for ticklist in ticklists:
        filepath = 'Data/ticklists/'+ticklist
        climber_name = ' '.join(ticklist.split('_')[:2]).title()
        process_csv_ticklist(climber_name, filepath)
