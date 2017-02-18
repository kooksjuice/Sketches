# hw1pr3.py
# Anna Novikova
# 02/04/17

import csv
from collections import *
import re

#
# readcsv is a starting point - it returns the rows from a standard csv file...
#
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



#
# write_to_csv shows how to write that format from a list of rows...
#  + try   write_to_csv( [['a', 1 ], ['b', 2]], "smallfile.csv" )
#
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

#function takes in a csv file with two rows of words and returns a dictionary with first row
#words as keys and seond row words as values
def text_subs(csv_file):
    LoR = readcsv(csv_file)
    subsD = defaultdict(str)
    for row in LoR:
        orig = row[0]
        sub = row[1]
        subsD[orig] = '<mark class="red">' + sub +'</mark>'
    return subsD
    


#function substitutes words in text accourding to dictionary subs
def annotate_text( text, subs ):
    
    pattern = re.compile(r'\b(' + '|'.join(subs.keys()) + r')\b')
    new_text = pattern.sub(lambda x: subs[x.group()], text)
        
    return new_text

# 
def annotate_text_to_html(text_path, subs_path, html_file):
    original = open(text_path).read()
    annotated = annotate_text(original, text_subs(subs_path))
    
    f= open(html_file,"w")
    html_str = ''
    html_str += '<html>'
    html_str += '<head>'
    html_str += '<style>'
    html_str += 'mark.red {color:red}'
    html_str += '</style>'
    html_str += '<title>Substitutions!</title>'
    html_str += '</head>'
    html_str += '<body>'
    html_str += '<h2>Comparing...</h2>'
    html_str += '<br>'
    html_str += '<h3>Original:</h3>'
    html_str += '<p>'
    html_str += original
    html_str += '</p>'
    html_str += '<br>'
    html_str += '<h3>Annotated:</h3>'
    html_str += '<p>'
    html_str += annotated
    html_str += '</p>'
    html_str += '</body>'
    html_str += '</html>'
    f.write(html_str)
    f.close()
    
#change subs_path, html_path and text_path to appropriate ones, keeping the names of files
#and run
def main():
    subs_path = '/Users/Mac/Google Drive/CS35/hw1/subs_list.csv'
    html_path = '/Users/Mac/Google Drive/CS35/hw1/annotated_html.html'
    text_path = '/Users/Mac/Google Drive/CS35/hw1/test_text.txt'
    annotate_text_to_html( text_path, subs_path, html_path )
