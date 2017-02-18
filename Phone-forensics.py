
# Anna Novikova
# 
# Analyzing 10,000 phone book entries!
#
# Questions:
# How many .txt files are in the whole set?
# Across all of the files, how many of the phone numbers contain exactly 10 digits? 
# How many people have the name "GARCIA" in the whole set?
# What is the longest name?
# What is the largest sum of digits?
# How many number entries use brackets and dashes?

import os


#function counts number of files in all subdirectories of a directory with a given path
def count_files(path):
    count = 0
    folders = ([name for name in os.listdir(path) if not (name.startswith('.')) and (name.format('.txt'))]) 
    for folder in folders:
        count += len(os.listdir(os.path.join(path,folder)))
    return count

#function returns the number of digits in the input string s  
def count_digits( s ):
    L = ['0','1','2','3','4','5','6','7','8','9']
    count = 0
    for i in s:
        if (i in L):
            count += 1
    return count

#function returns only the digits in the input string s
def clean_digits( s ):    
    L = ['0','1','2','3','4','5','6','7','8','9']
    temp = []
    for i in s:
        if (i in L):
            temp += i
    return ''.join(temp)

#function counts how many of phone numbers contain exactly 10 digits
def count_10dig(path):
    count = 0
    folders = ([name for name in os.listdir(path) if not (name.startswith('.')) and (name.format('.txt'))]) 
    for folder in folders:
        file_names = os.listdir(os.path.join(path,folder))
        for file in file_names:
            contents = open(os.path.join(path,folder,file)).read()
            if count_digits(contents) == 10:
                count += 1
    return count

#function counts how many of phone numbers contain exactly 10 digits and start with 909
def count_10dig_909(path):
    count = 0
    folders = ([name for name in os.listdir(path) if not (name.startswith('.')) and (name.format('.txt'))]) 
    for folder in folders:
        file_names = os.listdir(os.path.join(path,folder))
        for file in file_names:
            contents = open(os.path.join(path,folder,file)).read()
            if count_digits(contents) == 10 and (contents.startswith('909') or contents.startswith('(909')):
                count += 1
    return count

#function returns an all-lowercase, all-letter version of the input string s
def clean_word( s ):    
    L = ['0','1','2','3','4','5','6','7','8','9']
    temp = []
    for i in s:
        if not (i in L):
            temp += i
    return ''.join(temp).lower()

#function counts the number of garcias in the directory
def count_garcia(path):
    count = 0
    folders = ([name for name in os.listdir(path) if not (name.startswith('.')) and (name.format('.txt'))]) 
    for folder in folders:
        file_names = os.listdir(os.path.join(path,folder))
        for file in file_names:
            contents = open(os.path.join(path,folder,file)).read()
            if "garcia" in clean_word(contents).lower():
                count += 1
    return count

# function finds longest first name
def find_long_name(path):
    length = 0
    name = ''
    folders = ([name for name in os.listdir(path) if not (name.startswith('.')) and (name.format('.txt'))]) 
    for folder in folders:
        file_names = os.listdir(os.path.join(path,folder))
        for file in file_names:
            contents = open(os.path.join(path,folder,file)).read()
            first = clean_word(contents).lower().split()[0]
            if len(first)>length:
                length = len(first)
                name = first
    return name + 'is the longest first name'

# function finds the largest sum of digits
def largest_sum_digits(path):
    sum = 0
    folders = ([name for name in os.listdir(path) if not (name.startswith('.')) and (name.format('.txt'))]) 
    for folder in folders:
        file_names = os.listdir(os.path.join(path,folder))
        for file in file_names:
            temp = 0
            contents = open(os.path.join(path,folder,file)).read()
            list = clean_digits(contents).lower()
            for x in list:
                temp = int(x) + temp
            if sum < temp:
                sum = temp
    return sum

# functions finds the number of entries where numbers are written in (***) - *** - **** format
def count_dashes_and_brackets(path):
    count = 0
    folders = ([name for name in os.listdir(path) if not (name.startswith('.')) and (name.format('.txt'))]) 
    for folder in folders:
        file_names = os.listdir(os.path.join(path,folder))
        for file in file_names:
            contents = open(os.path.join(path,folder,file)).read()
            if "(" in contents and '-' in contents:
                count += 1
    return count



#path = '/Users/Mac/Google Drive/CS35/hw0/phone_files'
#main function that takes path of the phone_files folder
def main(path):
    count_files(path)
    count_10dig(path)
    count_10dig_909(path)
    count_garcia(path)
    find_long_name(path)
    count_dashes_and_brackets(path)
    largest_sum_digits(path)

