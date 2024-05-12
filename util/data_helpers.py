# This script contains utility functions for cleaning csv data 
# Filepaths are relative to main project folder
# By VR

import csv 

def find_max_lengths(filepath):
    """
    Console prints the longest char route name and location name from Routes.csv
    """
    with open(filepath, mode='r') as file:
        csv_file = csv.reader(file)
        next(csv_file)
        max_route_name = 0
        max_location = 0
        max_url = 0
        for line in csv_file:
            if len(line[0]) > max_route_name:
                max_route_name = len(line[0])
                max_name = line[0]
            if len(line[1]) > max_location:
                max_location = len(line[1])
                max_loc = line[1]
            if len(line[2]) > max_url:
                max_url = len(line[2])
        print(f'\nRoute Name max length: {max_route_name}; \n"{max_name}"\n')
        print(f'Location max chars: {max_location}; \n"{max_loc}"')
        print(f'Max URL: {max_url}')

def rating_cleanup(filepath):
    """
    Confirms data cleaning 
    """
    with open(filepath, mode='r') as file:
        csv_file = csv.reader(file)
        next(csv_file)
        for line in csv_file:
            print(line[5].split()[0])

def check_unique_names(filepath):
    """
    Console prints duplicate route names
    """
    routes = []
    with open(filepath, mode='r') as file:
        csv_file = csv.reader(file)
        next(csv_file)
        for line in csv_file:
            if line[0] not in routes:
                routes.append(line[0])
            else:
                print(f'{line[0]} is a duplicate at {line[1]}')

# find_max_lengths('Data/Routes.csv')
# rating_cleanup('Data/Routes.csv')
check_unique_names('Data/Routes.csv')