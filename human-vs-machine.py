#
# Person or machine?  The rps-string challenge...
#
# This file should includes code for 
#   + extract_features( rps ), returning a dictionary of features from an input rps string
#   + score_features( dict_of_features ), returning a score (or scores) based on that dictionary
#




# Here's how to machine-generate an rps string.

import random
import re
import collections
import csv
import numpy

def gen_rps_string( num_characters ):
    """ return a uniformly random rps string with num_characters characters """
    result = ''
    for i in range( num_characters ):
        result += random.choice( 'rps' )
    return result

# Here are two example machine-generated strings:
rps_machine1 = gen_rps_string(200)
rps_machine2 = gen_rps_string(200)
# print those, if you like, to see what they are...




from collections import defaultdict

def streaks(string):
    """function returns a list of all streaks of a single letter, which are more than 2"""
    p=re.compile('r{2,}|p{2,}|s{2,}')
    return p.findall(string)
    

def longest_streak(listic):
    """function takes in a list of streaks and returns maximum streak length"""

    if listic != []:
        return max(list(map(len, listic)))
    else:
        return 1
    
def all_streak_sum(listic):
    
    """function takes in a list of streaks and returns sum of all lenths of streaks"""
    
    if listic != []:
        return sum(list(map(len, listic)))
    else:
        return 1
    
def ratio_rps(string):
    
    """function returns the sum of distances from the ideal ratio"""

    d = collections.Counter(string)
    r = d['r']
    p = d['p']
    s = d['s']
    sums = r+p+s
    if sums != 0:
        return abs(1/3 - r/sums) + abs(1/3 - p/sums) + abs(1/3 - s/sums)
    else:
        return 0

        
    

#
# extract_features( rps ):   extracts features from rps into a defaultdict
#
def extract_features( rps ):
    """   extracts features from rps into a defaultdict
    """
    
    d = defaultdict( float )  
    d['rps'] = rps.count('rps')  
    d['long-streak'] = longest_streak(streaks(rps))
    d['ratio'] = ratio_rps(rps)
    d['all streak sum'] = all_streak_sum(streaks(rps))
    
    return d   # return our features... this is unlikely to be very useful, as-is






#
# score_features( dict_of_features ): returns a score based on those features
#
def score_features( dict_of_features ):
    """ Returns a score of humanness, the larger the score, the more human the answer is.
    """
    d = dict_of_features
    score = d['rps']*d['long-streak']*(d['ratio']+0.00001)*d['all streak sum']
    return numpy.log(score)







#
# read_data( filename="rps.csv" ):   gets all of the data from "rps.csv"
#
def read_data( filename="rps.csv" ):
    """ function read in the row with 'rsp' string from a rsp.csv
    """
  
    csvfile = open( filename, newline='' ) 
    csvrows = csv.reader( csvfile )              

    all_rows = []                               
    for row in csvrows:                         
        all_rows.append( row[3] )

    del csvrows                                 
    csvfile.close()                              
                             

    return all_rows


def main():
    listic = []
    for i in read_data():
        listic.append(score_features(extract_features(i)))
    return listic

