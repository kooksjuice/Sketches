
#
# Anna Novikova
#
# Here I analyzed all Inaugural Adsresses to answer some questions I was curious about.
#
# Questions:
# Comparing 2009's and 2013's addresses, which used the word "country" more often?
# Comparing all of the addresses, which used the word "war" most often?
# Which of the addresses contains the largest number of four-letter words? 
# which speech uses most numbers?
# what is the shortest speech?
# what is the longest word and what file it occurs in?

import re, string, timeit, os


#function returns the number of digits in the input string s  
def count_digits( s ):
    L = ['0','1','2','3','4','5','6','7','8','9']
    count = 0
    for i in s:
        if (i in L):
            count += 1
    return count

# count number of occurences of a word in a .txt file
def count_word(word, file_path):
    s = open(file_path).read()
    return s.lower().split().count(word)

# finds the key with maximum value in a dictionary
def key_of_max_value(dic):
    val=list(dic.values())
    key=list(dic.keys())
    return key[val.index(max(val))]

# function finds which file uses a given word the most times
def compare_file_word_counts(file_names, word):
    counts = {}
    for file in file_names:
        counts[file] = count_word(word, os.path.join(path, file))
    return key_of_max_value(counts) + ' uses word \'' + word + '\' most often in the given sample'

# function strips a string from punctiation
def no_punct( s ):    
    L = string.punctuation
    temp = []
    for i in s:
        if not (i in L):
            temp.append(i)
    return ''.join(temp).lower()

# function counts 4-letter words
def count_4letter_word(string):
    count = 0
    s = no_punct(string).split()
    for i in s:
        if len(i) == 4:
            count += 1
    return count

# function counts all words
def count_words(string):
    s = no_punct(string).split()
    return len(s)

# fucntion gives out file name that has the most 4-letter words
def compare_4_letter_word_counts(file_names):
    counts = []
    for file in file_names:
            counts.append(count_4letter_word(open(os.path.join(path, file)).read()))
    return 'file ' + file_names[counts.index(max(counts))] + ' has the most 4 letter words'

# function determines which file uses most digits (i.e. which president was the most analytically-thinking one)
def most_digits(file_names):
    counts = []
    for file in file_names:
            counts.append(count_digits(open(os.path.join(path, file)).read()))
    return 'file ' + file_names[counts.index(max(counts))] + ' has the most digits'

#function finds the shortest speech
def short_speech(file_names):
    counts = []
    for file in file_names:
            counts.append(count_words(open(os.path.join(path, file)).read()))
    return file_names[counts.index(min(counts))] + ' is the shortest speech'

#function finds the longest word in a string
def long_word(string):
    sum = 0
    word = ''
    s = no_punct(string).split()
    for i in s:
        if len(i)>sum:
            sum=len(i)
            word = i
    return word

# function finds the longest among all speeches
def longest_word(file_names):
    length = 0
    word = ''
    f = ''
    for file in file_names:
        temp = long_word(open(os.path.join(path, file)).read())
        if len(temp) > length:
            word = temp
            length = len(temp)
            f = file
    return 'longest word is ' + word + '. It occurs in file ' + file
        



#path = '/Users/Mac/Google Drive/CS35/hw0/addresses'
#main funciton that takes in the path of the addresses folder
def main(path):
    compare_file_word_counts(['2009.txt', '2013.txt'], 'country')
    compare_file_word_counts(os.listdir(path), 'war')
    compare_4_letter_word_counts(os.listdir(path))
    most_digits(os.listdir(path))
    longest_word(os.listdir(path))
