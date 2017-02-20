#
# Anna Novikova
#
#
# Datasets vs. People
# I want to compare if at any given time there are more datasets on data.gov than people.
# To do that I am going to:
# 1. scrape the data.gov page, 
# 2. scrape the API with active users of all data.gov websites
# 3. process the numbers from both and output the answer.

import json
import requests
from bs4 import BeautifulSoup

def people_scrape(filename_to_save="people.json"):
    
    lookup_url = "https://analytics.usa.gov/data/live/realtime.json"    
    parameters = {"data":"data"}    
    result = requests.get(lookup_url, params=parameters)
    data = result.json()

    # save to a file to examine it...
    f = open( filename_to_save, "w" )     # opens the file for writing
    string_data = json.dumps( data, indent=2 )  # this writes it to a string
    f.write(string_data)                        # then, writes that string to a file...
    f.close()                                   # and closes the file
    print("\nfile", filename_to_save, "written.")
    return

def dataset_scrape(url = 'https://www.data.gov/'):
    return requests.get(url).text
    
def get_people(filename_to_read="people.json"):
    f = open( filename_to_read, "r" )
    string_data = f.read()
    data = json.loads( string_data )
    return data['data'][0]['active_visitors']
    
    
def get_datasets(html):
    soup = BeautifulSoup(html, "html.parser")
    string = soup.findAll("a", {"href": "/metrics"})[0].string.split(' ')[0]
    return string.replace(',', '')

# main program that compares, it should give different answers 
#every 5 minutes, because the number of people is live
def compare():
    people_scrape(filename_to_save="people.json")
    html =dataset_scrape()
    dataset = get_datasets(html)
    people = get_people(filename_to_read="people.json")
    
    if people>dataset:
        temp = int(people) - int(dataset)
        print('There are currently ' + str(temp) + ' more people than datasets on data.gov website')
    elif people<dataset:
        temp =  int(dataset) - int(people)
        print('There are currently ' + str(temp) + ' more datasets than people on data.gov website')
    else:
        print('There are equal number of people and datasets on the data.gov website')
