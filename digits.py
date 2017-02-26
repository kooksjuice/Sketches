#
#
# digits.py
#
# Anna Novikova
#
#

import numpy as np
from sklearn import cross_validation
import pandas as pd
from sklearn.neighbors import KNeighborsClassifier
import matplotlib.pyplot as plt

# For Pandas's read_csv, use header=0 when you know row 0 is a header row
# df here is a "dataframe":
df = pd.read_csv('digits.csv', header=0)
df.head()
df.info()

# Convert feature columns as needed...
# You may to define a function, to help out:
def transform(s):
    """ from number to string
    """
    return 'digit ' + str(s)
    
df['label'] = df['64'].map(transform)  # apply the function to the column
print("+++ End of pandas +++\n")

# import sys
# sys.exit(0)

print("+++ Start of numpy/scikit-learn +++")

# Conversion to a numpy array
x_data_full = df.iloc[:,0:64].values        # iloc == "integer locations" of rows/cols
y_data_full = df.iloc[:,64].values      # also addressable by column name(s)


#
# now, we train the model with ALL of the training data...  and predict the labels of the test set
#
y_test_full = y_data_full[0:12]                  # the final testing outputs/labels (unknown)
X_test_full = X_data_full[0:12,0:64]              # the final testing data
y_test_part = y_data_full[12:22]                  # the final testing outputs/labels (unknown)
X_test_part = X_data_full[12:22,0:64]              # the final testing data

#
# we can scramble the remaining data
# 

X_train = X_data_full[22:,0:64]              # the training data        
y_train = y_data_full[22:]                  # the training outputs/labels (known)


indices = np.random.permutation(len(X_train))
X_train = X_train[indices]
y_train = y_train[indices]


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
    klist = list(range(1,10))
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
    
#
# From the results of running the function pick_num_neighbors, we see that the scores are maximum at k=3.
# To run the function an get the plot, uncomment the following line: 
# pick_num_neighbors()

#
# Now we fit knn to the whole training set with k=3.
#

knn = KNeighborsClassifier(n_neighbors=3)
knn.fit(X_train, y_train) 


#
# Predicting the full-data digits
#

knn.predict(X_test_full)





"""
Comments and results:

Briefly mention how this went:
  + what value of k did you decide on for your kNN?
  
  From the results of running the function pick_num_neighbors, we see that the scores are maximum at k=3.
  
  + how smoothly were you able to adapt from the iris dataset to here?
  
  The transition was smooth. It was not hard to adjust the code.
  
  + how high were you able to get the average cross-validation (testing) score?
  
  The average cv testing score was ~0.985



Then, include the predicted labels of the 12 digits with full data but no label:
Past those labels (just labels) here:
You'll have 12 lines:
0 
0 
0 
1 
7 
7 
7 
4 
0 
9 
9 
9



And, include the predicted labels of the 10 digits that are "partially erased" and have no label:
Mention briefly how you handled this situation!?

Erased in the analog world means blank space. So, I thought, there could be a situation like this,
so replacing them with zeros is a good option

Past those labels (just labels) here:
You'll have 10 lines:
5 
5 
6 
5 
0 
9 
8 
9 
8 
4


"""

