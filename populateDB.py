import csv
import sqlite3
from util import data_helpers
import uuid

def convert_YDS_to_int(yds_grade):
    """
    Accepts a climbing route difficulty in Yosemite Decimal System (YDS) and converts it 
    to int for SQL comparison
    """
    climbing_grades = {
        "5.1": 1,
        "5.1+": 1,
        "5.1-": 1,
        "5.2": 2,
        "5.2+": 2,
        "5.2-": 2,
        "5.3": 3,
        "5.3+": 3,
        "5.3-": 3,
        "5.4": 4,
        "5.4+": 4,
        "5.4-": 4,
        "5.5": 5,
        "5.5+": 5,
        "5.5-": 5,
        "5.6": 6,
        "5.6+": 6,
        "5.6-": 6,
        "5.7": 7,
        "5.7+": 7,
        "5.7-": 7,
        "5.8": 8,
        "5.8+": 8,
        "5.8-": 8,
        "5.9": 9,
        "5.9+": 9,
        "5.9-": 9,
        "5.10": 10,
        "5.10+": 10,
        "5.10-": 10,
        "5.10a": 10,
        "5.10a/b": 11,
        "5.10b": 12,
        "5.10b/c": 13,
        "5.10c": 14,
        "5.10c/d": 15,
        "5.10d": 16,
        "5.11": 17,
        "5.11+": 18,
        "5.11-": 17,
        "5.11a": 17,
        "5.11a/b": 19,
        "5.11b": 20,
        "5.11b/c": 21,
        "5.11c": 22,
        "5.11c/d": 23,
        "5.11d": 24,
        "5.12": 25,
        "5.12+": 26,
        "5.12-": 25,
        "5.12a": 25,
        "5.12a/b": 27,
        "5.12b": 28,
        "5.12b/c": 29,
        "5.12c": 30,
        "5.12c/d": 31,
        "5.12d": 32,
        "5.13": 33,
        "5.13+": 34,
        "5.13-": 33,
        "5.13a": 33,
        "5.13a/b": 35,
        "5.13b": 36,
        "5.13b/c": 37,
        "5.13c": 38,
        "5.13c/d": 39,
        "5.13d": 40,
        "5.14": 41,
        "5.14+": 42,
        "5.14-": 41,
        "5.14a": 41,
        "5.14a/b": 43,
        "5.14b": 44,
        "5.14b/c": 45,
        "5.14c": 46,
        "5.14c/d": 47,
        "5.14d": 48,
        "5.15": 49,
        "5.15+": 50,
        "5.15-": 49,
        "5.15a": 49,
        "5.15a/b": 51,
        "5.15b": 52,
        "5.15b/c": 53,
        "5.15c": 54,
        "5.15c/d": 55,
        "5.15d": 56
    }
    return climbing_grades[yds_grade]

def process_csv_routes(path):
    """
    Processes route entries into the DB
    """
    with sqlite3.connect('Database/MyClimb.db') as conn:
        cursor = conn.cursor()
        insert_query = '''
        INSERT INTO Routes (RouteName, Location, Region, URL, AVG_STARS, RouteType, Difficulty_Rating, Difficulty, Latitude, Longitude)
        VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?);
        '''
        with open(path, 'r') as file:
            routeDictionary = csv.DictReader(file)
            for row in routeDictionary:
                cursor.execute(insert_query, 
                                (row['Route'], 
                                row['Location'], 
                                row['Location'].split(' > ')[-1], # get the state portion of the location string
                                row['URL'], 
                                float(row['Avg Stars']), 
                                row['Route Type'], 
                                row['Rating'].split()[0], # clean out extra chars for danger tags
                                convert_YDS_to_int(row['Rating'].split()[0]),
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
                
def process_regions(path):
    """
    Processes climbing regions into the DB
    """
    with sqlite3.connect('Database/MyClimb.db') as conn:
        cursor = conn.cursor()
        insert_query = '''
        INSERT INTO Regions (Region, Country, Continent)
        VALUES (?, ?, ?);
        '''
        with open(path, 'r') as file:
            reader = csv.DictReader(file)
            for row in reader:
                cursor.execute(insert_query, 
                                (row['Region'], row['Country'], row['Continent']))  
                
def process_common_geologies(path):
    """
    Processes common geologies into the DB
    """
    with sqlite3.connect('Database/MyClimb.db') as conn:
        cursor = conn.cursor()
        insert_query = '''
        INSERT INTO Common_geologies (Region, MainGeology)
        VALUES (?, ?);
        '''
        with open(path, 'r') as file:
            reader = csv.DictReader(file)
            for row in reader:
                cursor.execute(insert_query, 
                                (row['Region'], row['Rock Type']))  
                
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

write_routes()