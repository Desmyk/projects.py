# import requests library
import requests
# import csv library to handle CSV  files
import csv

# Define a function to fetch data from given endpoint
def fetch_rick_and_morty_data(endpoint):
    
    # send GET request to endpoint
    response = requests.get(endpoint)
    
    # parse response as json
    data = response.json()
    # rturn the data
    return data

# Define function to save data to CSV file
def save_to_csv(data, filename):
    # open file in Write mode
    with open(filename, 'w', newline='') as csvfile:
        
        # Define the fieldnames
        fieldnames = ['id', 'name']
        
        # create DictWriter object
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        
        # create header and write it to the CSV file
        writer.writeheader()
        
        # loop through the data and write a row for each item\entities
        for item in data:
            writer.writerow({'id': item['id'], 'name': item['name']})

# Define the API endpoints (characters, locations and episodes)
characters_endpoint = "https://rickandmortyapi.com/api/character/"
locations_endpoint = "https://rickandmortyapi.com/api/location/"
episodes_endpoint = "https://rickandmortyapi.com/api/episode/"

# Fetch data from the API
characters_data = fetch_rick_and_morty_data(characters_endpoint)
locations_data = fetch_rick_and_morty_data(locations_endpoint)
episodes_data = fetch_rick_and_morty_data(episodes_endpoint)

# Save data to CSV files
save_to_csv(characters_data["results"], "characters.csv")
save_to_csv(locations_data["results"], "locations.csv")
save_to_csv(episodes_data["results"], "episodes.csv")

# read  characters.csv file and print output
with open('characters.csv', 'r') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        print(row)

# read locations.csv file and print output        
with open('locations.csv', 'r') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        print(row)

# read episodes.csv file and print output        
with open('episodes.csv', 'r') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        print(row)