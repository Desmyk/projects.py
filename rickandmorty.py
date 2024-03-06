# Import the csv module
import csv 
# Import the json module
import json 
# Import the requests module
import requests 

# Define the number of entries to fetch for each entry type
num_entries = 20 

# Define the base URL for the Rick and Morty API
base_url = "https://rickandmortyapi.com/api/" 

# Define a function to fetch and save data for a given entry type
def fetch_save_data(entry_type):
    
    # Define the URL for the API endpoint 
    url = base_url + entry_type 
    
    # Send an HTTP GET request to the url
    r = requests.get(url) 
    
    # Convert the response to JSON format
    data = r.json() 
    
     # Define the list of fieldnames to write to the CSV file
    fieldnames = ['id', 'name'] 
    
    # Define the file name for the CSV file
    filename = f'{entry_type.lower()}.csv' 

    # Open the CSV file in write mode
    with open(filename, 'w', newline='') as f: 
        # Create a CSV writer object
        writer = csv.DictWriter(f, fieldnames=fieldnames) 
        # Write the header to the CSV file
        writer.writeheader()
        # Write the data to the CSV file
        writer.writerows([{'id': item['id'], 'name': item['name']} for item in data['results']]) 

fetch_save_data('character')
# Call the function to fetch and save character data
fetch_save_data('location') 
# Call the function to fetch and save location data
fetch_save_data('episode') 
# Call the function to fetch and save episode data


# Open the character.csv file in read mode
with open('character.csv', mode='r', newline='') as f: 
     reader = csv.DictReader(f)
     # iterate through the rows in CSV file
     for row in reader:
     # print contents of row
        print(row)
        
 
 # Open the location.csv file in read mode
with open('location.csv', mode='r', newline='') as f: 
     # Create a CSV reader object
     reader = csv.DictReader(f)
     # iterate through the rows in CSV file
     for row in reader:
     # print contents of row
        print(row)
        
        
# Open the episode.csv file in read mode
with open('episode.csv', mode='r', newline='') as f: 
     # Create a CSV reader object
     reader = csv.DictReader(f)
     # iterate through the rows in CSV file
     for row in reader:
     # print contents of row
        print(row)
        
               
