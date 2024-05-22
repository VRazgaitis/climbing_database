# This script contains utility functions for cleaning csv data 
# Filepaths are relative to main project folder

import csv 
import os
from util import web_scraping

def find_max_lengths(filepath):
    """
    Console prints the longest char route name and location name from a csv containing routes data
    """
    with open(filepath, mode='r') as file:
        csv_file = csv.reader(file)
        next(csv_file)
        max_route_name = 0
        max_location = 0
        max_url = 0
        max_lat = 0
        max_long = 0
        for line in csv_file:
            if len(line[0]) > max_route_name:
                max_route_name = len(line[0])
                max_name = line[0]
            if len(line[1]) > max_location:
                max_location = len(line[1])
                max_loc = line[1]
            if len(line[2]) > max_url:
                max_url = len(line[2])
            if len(line[9]) > max_lat:
                max_lat = len(line[9])
            if len(line[10]) > max_long:
                max_long = len(line[10])
        print(f'\nRoute Name max length: {max_route_name}; \n"{max_name}"\n')
        print(f'Location max chars: {max_location}; \n"{max_loc}"')
        print(f'Max URL: {max_url}')
        print(f'Max lat, long: {max_lat, max_long}')

def rating_cleanup(filepath):
    """
    Confirms data cleaning on Rating attribute.
    5.9+ PG13 is a rating string that conatins both difficulty (5.9+) and danger (PG13)
    Our dataset should contain only difficulty and not danger
    """
    with open(filepath, mode='r') as file:
        csv_file = csv.reader(file)
        next(csv_file)
        for line in csv_file:
            print(line[5].split()[0])

def check_unique_names(filepath):
    """
    Console prints duplicate route names in csv files
    """
    routes = []
    with open(filepath, mode='r') as file:
        csv_file = csv.reader(file)
        next(csv_file)
        for line in csv_file:
            if line[0] not in routes:
                routes.append(line[0])
            else:
                print(f'DUPLICATE ROUTENAME: {line[0]}; 2ND LOCATION: {line[1]}')

def list_filenames(directory):
    """
    Lists all filenames in a specified directory
    Used for batch writting data into DB
    """
    try:
        # Get a list of all files and directories in specified directory
        items = os.listdir(directory)
        # Filter out directories, keeping only files
        filenames = [item for item in items if os.path.isfile(os.path.join(directory, item))]
        return filenames
    
    except Exception as e:
        print(f"An error occurred: {e}")
        return []

def max_notes_length():
    """
    Prints the longest note length, note, from all climber ticklists in the Data/ticklists folder
    """
    directory_path = 'Data/ticklists'
    file_list = list_filenames(directory_path)
    max_note = 0
    for ticklist in file_list:
        print(f"\n{' '.join(ticklist.split('_')[:2]).title()} Climbs:")  # pull climber's {Fname Lname} from fname_lname_ticklist.csv  
        with open(directory_path + '/' + ticklist, mode='r') as file:
            csv_file = csv.reader(file)
            next(csv_file)
            for line in csv_file:
                if len(line[3]) > max_note:
                    text_string = line[3]
                    max_note = len(line[3]) 
                print(line[1])
    print(max_note, text_string)

def extract_name(ticklist):
    """
    pull climber's {Fname Lname} from fname_lname_ticklist.csv
    """
    print(f"\n{' '.join(ticklist.split('_')[:2]).title()} Climbs:")  

def extract_state(path):
    """
    extract the region out of the location string
    """
    with open(path, 'r') as file:
        tickDictionary = csv.DictReader(file)
        for row in tickDictionary:
            print(row['Location'].split(' > ')[-1])

def scraper_demo():
    directory_path = 'Data/Routes/RRG_nc.csv'
    with open(directory_path, mode='r') as file:
        csv_file = csv.reader(file)
        next(csv_file)
        for line in csv_file:
            img=web_scraping.scrape_MP_route_img(line[2])[0]
            print(img)
