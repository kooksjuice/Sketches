
#
# Anna Novikova
#
# Accessing iTunes API and running comparison tests on the number of records for two artists. 
#

import requests
import json
import string

def apple_api_id_scraper(artist_name, filename_to_save="appledata_id.json"):
    """ 
    """
    ### Use the search url to get an artist's itunes ID
    search_url = "https://itunes.apple.com/search"
    parameters = {"term":artist_name, "entity":"musicArtist","media":"music","limit":200, "artistId":"artistId"}
    result = requests.get(search_url, params=parameters)
    data = result.json()

    # save to a file to examine it...
    f = open( filename_to_save, "w" )     # opens the file for writing
    string_data = json.dumps( data, indent=2 )  # this writes it to a string
    f.write(string_data)                        # then, writes that string to a file...
    f.close()                                   # and closes the file
    print("\nfile", filename_to_save, "written.")

    # we'll return a useful value: the artist id...
    #
    # Note: it's helpful to find the iTunes artistid and return it here
    # (this hasn't been done yet... try it!) 

    return data['results'][0]['artistId']  # This is the Beatles...


#
# 
#
def apple_api_full_scraper(artistid, filename_to_save="appledata_full.json"):
    """ 
    Takes an artistid and grabs a full set of that artist's albums.
    "The Beatles"  has an id of 136975
    """
    lookup_url = "https://itunes.apple.com/lookup"    
    parameters = {"entity":"album","id":artistid}    
    result = requests.get(lookup_url, params=parameters)
    data = result.json()

    # save to a file to examine it...
    f = open( filename_to_save, "w" )     # opens the file for writing
    string_data = json.dumps( data, indent=2 )  # this writes it to a string
    f.write(string_data)                        # then, writes that string to a file...
    f.close()                                   # and closes the file
    print("\nfile", filename_to_save, "written.")

    # we'll leave the processing to another function...
    return



#
#
#
def apple_api_full_process(filename_to_read="appledata_full.json"):
    """ example of extracting one (small) piece of information from 
        the appledata json file...
    """
    f = open( filename_to_read, "r" )
    string_data = f.read()
    data = json.loads( string_data )
    #print("data (not spiffified!) is\n\n", data, "\n")

    # for live investigation, here's the full data structure
    return data


def most_productive_scrape(artist1, artist2, fname1="artist1.json", fname2="artist2.json"):
    """function scrapes the iTunes API first to find the artist IDs 
    and then to access all informaiton about them
    """
    id1 = apple_api_id_scraper(artist1)
    apple_api_full_scraper(id1,fname1)
    
    id2 = apple_api_id_scraper(artist2)
    apple_api_full_scraper(id2,fname2)
    return


def most_productive_process(fname1="artist1.json", fname2="artist2.json"):
    #"""function counts how many worksa are present by the two artists in question"""
    
    data1 = apple_api_full_process(fname1)
    artist1 = data1['results'][0]['artistName']
    res1 = data1['resultCount']
    
    data2 = apple_api_full_process(fname2)
    artist2 = data2['results'][0]['artistName']
    res2 = data2['resultCount']
    
    print("There are", res1, "works by", artist1, "in iTunes Store")
    print("There are", res2, "works by", artist2, "in iTunes Store")
    return


""" Tests I ran
most_productive_scrape( "alt-J", "The Kooks" )
most_productive_process() 
most_productive_scrape( "MGMT", "Vance Joy" )
most_productive_process()
most_productive_scrape( "Queen", "The Glass Animals" )
most_productive_process()

"""
