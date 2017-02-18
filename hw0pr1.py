
# coding: utf-8

# In[12]:

# hw0pr1.py
# 
# Anna Novikova (started in class with Albert Xu)
# completed in Jupyter Notebooks



#function prints the string s 42 times (on separate lines)
def times42( s ):      
    for i in range(41):
        print(s)

#function returns the string "aliii...iiien" with exactly N "i"s
def alien( N ):
    print("al"+N*"i"+"en")

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

#function returns an all-lowercase, all-letter version of the input string s
def clean_word( s ):    
    L = ['0','1','2','3','4','5','6','7','8','9']
    temp = []
    for i in s:
        if not (i in L):
            temp += i
    return ''.join(temp).lower()

