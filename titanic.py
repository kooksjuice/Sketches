#
#
# titanic.py
#
# Anna Novikova

import numpy as np
from sklearn import datasets
from sklearn import cross_validation
import pandas as pd
from sklearn.neighbors import KNeighborsClassifier
import matplotlib.pyplot as plt


# For Pandas's read_csv, use header=0 when you know row 0 is a header row
# df here is a "dataframe":
df = pd.read_csv('titanic.csv', header=0)


# let's drop columns with too few values or that won't be meaningful
# Here's an example of dropping the 'body' column:
df = df.drop('body', axis=1)
df = df.drop('name', axis=1)
df = df.drop('ticket', axis=1)
df = df.drop('cabin', axis=1)
df = df.drop('home.dest', axis=1)
df = df.drop('boat', axis=1)
df = df.drop('embarked', axis=1)


# let's drop all of the rows with missing data:
df = df.dropna()


# You'll need conversion to numeric datatypes for all input columns
#   Here's one example
#
def tr_mf(s):
    """ from string to number
    """
    d = { 'male':0, 'female':1 }
    return d[s]
def tr_survival(i):
    """from int to word
    1 -> survived 
    0 -> did not survive
    """
    d = { 0:'did not survive', 1: 'survived' }
    return d[i]
    

df['sex'] = df['sex'].map(tr_mf)  # apply the function to the column

# import sys
# sys.exit(0)


# We'll stick with numpy - here's the conversion to a numpy array

# extract the underlying data with the values attribute:
X_data = df.drop('survived', axis=1).values        # everything except the 'survival' column
y_data = df[ 'survived' ].values      # also addressable by column name(s)


#
# test inputs
#
X_test = X_data[0:42]

#
# training data
#
X_train = X_data[42:]
y_train = y_data[42:]






#
# Funtions to help with cross validation and decisions
# 

def cv_n_times(n, knn):
    """function runs cross validation on the set n number of times"""
    train = 0
    test = 0
    for i in range(n):
        cv_data_train, cv_data_test, cv_target_train, cv_target_test =             cross_validation.train_test_split(X_train, y_train, test_size=0.5)
        knn.fit(cv_data_train, cv_target_train)
        train += knn.score(cv_data_train, cv_target_train)
        test += knn.score(cv_data_test, cv_target_test)
    #average fit score for training sets
    avgTrain = train/n
    #average fit score for test sets
    avgTest = test/n
    return avgTrain, avgTest

def pick_num_neighbors():
    """function when run, plots training and testing scores. It is easy to see from the graph which k to use. """
    klist = list(range(1,30))
    scoresTR = []
    scoresTE = []
    for i in klist:
        knn = KNeighborsClassifier(n_neighbors=i)
        avgTR, avgTE = cv_n_times(10, knn)
        scoresTR.append(avgTR)
        scoresTE.append(avgTE)
    plt.plot(klist, scoresTR, label = 'training scores')
    plt.plot(klist, scoresTE, label = 'test scores')
    plt.ylabel("Score Value")
    plt.xlabel("Number of Neighbors")
    plt.title('KNN Scores')
    plt.legend()
    plt.show()

    
def plot_feature_eng_scores():
    """the function increases imporatance of each feature by 10000 one at a time
    and plots a graph with scores for various values of neighbors"""
    for i in range(len(X_data[0])):
        X_data[:,i]  *= 10000
        print('Feature ' + str(i) + ' is increased by 10000')
        pick_num_neighbors()
        X_data[:,i] /= 10000

        
#
# the rest of this model-building, cross-validation, and prediction will come here:
#     
#

plot_feature_eng_scores()

# implementing plot_feature_eng_scores(), I saw an increase in test scores for feature 1, thus:

X_data[:,1]  *= 10000
print("++ After increasing Feature 1 by 100000 ++")
plot_feature_eng_scores()

# after increaing feature 1, I re-ran the test, increasing the importance of each feature by 100 again 
# and found that increase in feature 0 is adding an improvement

X_data[:,0]  *= 10000
print("++ After increasing Feature 0 by 100000 ++")
plot_feature_eng_scores()

# after that there wasn't much improvement.
# So I ran the test to pick the best number of neighbors for the model
pick_num_neighbors()

# and saw that k=6 is the best one. From one run to another, the best k was either 6,7 or 8.
# I assumed the less k is the better, and picked 6. 

knn = KNeighborsClassifier(n_neighbors=7)
knn.fit(X_train, y_train)
output = knn.predict(X_test)

#
#printing out survival status of each the 42 unknown passengers
#
for i in output:
    print(tr_survival(i))


"""
Comments and results:

  + what value of k did you decide on for your kNN?
    I saw that k=6 is the best one. From one run to another, the best k was either 6,7 or 8.
    I assumed the less k is the better, and picked 6. 
  
  + how high were you able to get the average cross-validation (testing) score?
    I was able to get the test scores to ~ .8


The predicted survival of the 42 passengers with unknown status:
did not survive
did not survive
did not survive
did not survive
did not survive
did not survive
did not survive
survived
survived
survived
survived
survived
did not survive
survived
did not survive
did not survive
did not survive
did not survive
did not survive
did not survive
did not survive
survived
did not survive
survived
survived
survived
did not survive
did not survive
survived
did not survive
did not survive
did not survive
survived
survived
did not survive
did not survive
survived
survived
did not survive
survived
did not survive
survived




"""


