
# coding: utf-8

# In[ ]:

The iTunes store gives API access to searching for artists, albums, movies, etc. 
This week’s starter file includes code to lookup the iTunes ID for an artist 
(in our case, The Beatles) and then to use that ID in order to retrieve a list of all 
of the albums in the iTunes store for that artist. 

Skim over the API Documentation to get an idea of what else you can do with 
the iTunes Store API.

Write a pair of functions (in a spirit similar to the starter code):
most_productive_scrape(artist1, artist2, fname1="artist1.json", fname2="artist2.json")   
that takes the names of two artists as input, converts those names to AppleIDs 
(notice that this requires an API call!) and then makes another API call in order 
to gather all of the album/work information from iTunes. It should save those results 
into the filenames fname1 and fname2 (with reasonable defaults, as you see above).  

For example, calling   most_productive_scrape("Steve Perry", "Katy Perry")  should
get cross-generational "Perry" information into those two files...   

Then, write
most_productive_process(fname1="artist1.json", fname2="artist2.json")  
which reads in those two files and then prints out (a) the artists and (b) 
the number of works they have in the iTunes store.  You'll need to look the artists' 
names from the json files - this is pretty typical, even if it feels backwards! 
For reference, here is what prints out when these two functions are run in 
our solutions (feel free to alter what's printed, of course). Also, 
remember that most of the work is behind the scenes in the json files

Python code:  
most_productive_scrape("Steve Perry", "Katy Perry")
file artist1.json written.
file artist2.json written.
most_productive_process()
               
num of results for Steve Perry == 9
num of results for Katy Perry == 31
 
Be sure to include a docstring for each function describing (briefly) what it does...
Include at least three test cases 
comparing interesting pairs of artists of your own choosing… !


# In[ ]:




# In[ ]:




# In[ ]:




# In[ ]:




# In[ ]:



