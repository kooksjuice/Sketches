
# coding: utf-8

# In[18]:

# hw2pr1.py
#
# Anna Novikova
#
# CS35, 02/12/17

import requests
import string
import json


def multicity_distance_scrape( Origins, Dests, filename_to_save="multicity.json" ):
    
    url="http://maps.googleapis.com/maps/api/distancematrix/json"

    orig = "|".join(Origins)
    dest = "|".join(Dests)
    my_mode="driving"

    inputs={"origins":orig,"destinations":dest,"mode":my_mode}

    result = requests.get(url,params=inputs)
    data = result.json()
    print("data is", data)

    # save this json data to file
    f = open( filename_to_save, "w" )     
    string_data = json.dumps( data, indent=2 )  
    f.write(string_data)                        
    f.close()                                   
    print("\nfile", filename_to_save, "written.")
    return


def multicity_distance_process(filename_to_read = "multicity.json"):
    """ 
    function reads in a json file and outputs html code of a table with 
    """
    f = open( filename_to_read, "r" )
    string_data = f.read()
    data = json.loads( string_data )
    print("data (not spiffified!) is\n\n", data, "\n")

    html_string = "<table>"

    rows = data["rows"]
    dest = data["destination_addresses"]
    orig = data["origin_addresses"]
    o = 0
    
    html_string += "<tr>"
    html_string += "<td>"
    html_string += ""
    html_string += "</td>"
    for d in dest:
        html_string += "<td>"
        html_string += d
        html_string += "</td>"
    html_string += "</tr>" 
    
    for row in rows:
        html_string += "<tr>"
        html_string += "<td>"
        html_string += orig[o]
        html_string += "</td>"
        elements = row["elements"]
        for elem in elements:
            html_string += "<td>"
            html_string += elem["distance"]["text"]
            html_string += "</td>"
        html_string += "</tr>"
        o += 1
    html_string += "</table>"

    return html_string


#
# a main function for problem 1 (the multicity distance problem)
#
def main():
    """ 
    main function with tests from class
    """
    Origins = ['Pittsburgh,PA','Boston,MA','Seattle,WA']
    Dests = ['Claremont,CA','Atlanta,GA'] 
    multicity_distance_scrape( Origins, Dests, filename_to_save="multicity.json" )
    multicity_distance_process(filename_to_read = "multicity.json")

