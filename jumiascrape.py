import requests
from bs4 import BeautifulSoup

url = 'https://www.jumia.co.ke/'

# using try-except block to handle any exceptions that may occur during the execution of the code
try:
    # send request to website
    r = requests.get(url)

    #parse the HTML content
    soup = BeautifulSoup(r.content, 'html.parser')


    # find items on the page using class name 
    item_name = soup.find_all('div', class_ = 'name')

    # find prices on the page using class name 
    prices = soup.find_all('div', class_ = 'prc')

    # find num of units left on the page using class name
    units_left = soup.find_all('div', class_ = 'stk')

    # iteration over the list of 'item name', prints corresponding prices and units left
    for i in range(len(item_name)):
        print(f"Item Name: {item_name[i].text.strip()}, Price: {prices[i].text.strip()}, Units Left: {units_left[i].text.strip()}")
        
# provides exception for index out of range error if there is a mismatch
except Exception as e:
    print(f'error occurred: {e}')