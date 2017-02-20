#
# Anna Novikova
# 
# Simple Text Analysis from csv file. Unweighted and Weighted word counts. 
# Cretin output to generate HTML table.
#

import csv
from collections import *
import numpy as np

def readcsv( csv_file_name ):
    """ readcsv takes as
         + input:  csv_file_name, the name of a csv file
        and returns
         + output: a list of lists, each inner list is one row of the csv
           all data items are strings; empty cells are empty strings
    """
    try:
        csvfile = open( csv_file_name, newline='' )  # open for reading
        csvrows = csv.reader( csvfile )              # creates a csvrows object

        all_rows = []                               # we need to read the csv file
        for row in csvrows:                         # into our own Python data structure
            all_rows.append( row )                  # adds only the word to our list

        del csvrows                                  # acknowledge csvrows is gone!
        csvfile.close()                              # and close the file
        return all_rows                              # return the list of lists

    except FileNotFoundError as e:
        print("File not found: ", e)
        return []
    
def write_to_csv( list_of_rows, filename ):
    """ readcsv takes as
         + input:  csv_file_name, the name of a csv file
        and returns
         + output: a list of lists, each inner list is one row of the csv
           all data items are strings; empty cells are empty strings
    """
    try:
        csvfile = open( filename, "w", newline='' )
        filewriter = csv.writer( csvfile, delimiter=",")
        for row in list_of_rows:
            filewriter.writerow( row )
        csvfile.close()

    except:
        print("File", filename, "could not be opened for writing...")
        


#unweighted counting of first letters!
def UWcount():
    """ returns a dictionary (defaultdict) of
        unweighted first-letter counts from 
        the file wds.csv
    """
    LoR = readcsv( '/Users/Mac/Google Drive/CS35/hw1/cs35_hw1_all_starters/wds.csv' )  # List of rows
    #print("LoR is", LoR)
    counts = defaultdict(int)
    for Row in LoR:
        word = str(Row[0])      # the word is at index 0
        num  = float(Row[1])    # its num occurrences is at index 1
        first_letter = word[0]  # the first letter of the word
        counts[first_letter] += 1   # add one to that letter's counts
    # done with for loop
    return counts

# function inputs a path of a file, and outputs weighted counts of the first letters
def W_first_count(path):
    
    LoR = readcsv( path )  # List of rows
    #print("LoR is", LoR)
    counts = defaultdict(float)
    weights = defaultdict(float)
    weighted =  defaultdict(float)
    total_words = 0
    for Row in LoR:
        num  = float(Row[1])
        total_words = total_words + num
    for Row in LoR:
        word = str(Row[0])      # the word is at index 0
        num  = float(Row[1])    # its num occurrences is at index 1
        first_letter = word[0]  # the first letter of the word
        counts[first_letter] += 1
        weights[first_letter] += 1-num/total_words   # add one to that letter's counts
    for x in counts:
        weighted[x] = counts[x]*weights[x]
    # done with for loop
    return weighted

# function inputs a path of a file, and outputs weighted counts of the last letters
def W_last_count(path):
    
    LoR = readcsv( path )  # List of rows
    #print("LoR is", LoR)
    counts = defaultdict(float)
    weights = defaultdict(float)
    weighted =  defaultdict(float)
    total_words = 0
    for Row in LoR:
        num  = float(Row[1])
        total_words = total_words + num
    for Row in LoR:
        word = str(Row[0])      # the word is at index 0
        num  = float(Row[1])    # its num occurrences is at index 1
        last_letter = word[-1]  # the first letter of the word
        counts[last_letter] += 1
        weights[last_letter] += 1-num/total_words   # add one to that letter's counts
    for x in counts:
        weighted[x] = counts[x]*weights[x]
    # done with for loop
    return weighted

# function inputs a path of a file, and outputs weighted counts of the second letters
def W_second_count(path):
    
    LoR = readcsv( path )  # List of rows
    #print("LoR is", LoR)
    counts = defaultdict(float)
    weights = defaultdict(float)
    weighted =  defaultdict(float)
    total_words = 0
    for Row in LoR:
        word = str(Row[0])
        num  = float(Row[1])
        if len(word) > 1:
            total_words = total_words + num
    for Row in LoR:
        word = str(Row[0])      # the word is at index 0
        num  = float(Row[1])    # its num occurrences is at index 1
        if len(word) > 1:
            second_letter = word[1]  # the first letter of the word
            counts[second_letter] += 1
            weights[second_letter] += 1-num/total_words   # add one to that letter's counts
    for x in counts:
        weighted[x] = counts[x]*weights[x]
    # done with for loop
    return weighted

#function creates a list of frequencies of each letter
def create_list_freq(path):
    first = W_first_count(path)
    last = W_last_count(path)
    second = W_second_count(path)
    listic = [['letter', 'first', 'last', 'second']]
    for k in first:
        listic.append([k, first[k], last[k], second[k]])
    return listic

# takes in csv path and html output path and creates a table in html from the csv
def csv_to_html_table(csvfile, html_file):
    LoR = readcsv(csvfile)             
 
    f= open(html_file,"w")
    html_string = '<table>\n'    
    for row in LoR:                         
        html_string += '<tr>\n'
        for x in row:
            html_string += '<td>'+ str(x) + '</td>'
        html_string += '</tr>\n'
    html_string += '</table>\n'
    f.write(html_string)
    f.close()
    return html_string
    
    



# main function that takes in input file (wds.csv) and creates two output files (frequencies.csv, letter_frequencies.html)
def main(input_file, csv_file, html_file):
    write_to_csv(create_list_freq(input_file), csv_file)
    csv_to_html_table(csv_file, html_file)


#example of how to run main
#i_path = '/Users/Mac/Google Drive/CS35/hw1/cs35_hw1_all_starters/wds.csv'
#o_path = '/Users/Mac/Google Drive/CS35/hw1/cs35_hw1_all_starters/frequencies.csv'
#html_path = '/Users/Mac/Google Drive/CS35/hw1/cs35_hw1_all_starters/letter_frequencies.html'
#main(i_path, o_path, html_path)
