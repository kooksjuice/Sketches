#
# iris.py
#
# Anna Novikova
# 02/27/17

import numpy as np
from sklearn import cross_validation
import pandas as pd
from sklearn.neighbors import KNeighborsClassifier
import matplotlib.pyplot as plt

print("+++ Start of pandas +++\n")
df = pd.read_csv('iris.csv', header=0)    # read the file
df.head()                                 # first five lines
df.info()                                 # column details


# One important feature is the conversion from string to numeric datatypes!
# As input features, numpy and scikit-learn need numeric datatypes
# We can define a transformation function, to help out...
def transform(s):
    """ from string to number
          setosa -> 0
          versicolor -> 1
          virginica -> 2
    """
    d = { 'unknown':-1, 'setosa':0, 'versicolor':1, 'virginica':2 }
    return d[s]
    
# 
# this applies the function transform to a whole column
#
df['irisname'] = df['irisname'].map(transform)  # apply the function to the column

print("+++ End of pandas +++\n")

print("+++ Start of numpy/scikit-learn +++")
# Data needs to be in numpy arrays - these next two lines convert to numpy arrays
X_data_full = df.iloc[:,0:4].values        # iloc == "integer locations" of rows/cols
y_data_full = df[ 'irisname' ].values      # individually addressable columns (by name)


#
# we can drop the initial (unknown) rows -- if we want to test with known data
X_data_full = X_data_full[9:,:]   # 2d array
y_data_full = y_data_full[9:]     # 1d column


#
# we can scramble the remaining data if we want - only if we know the test set's labels
# 
indices = np.random.permutation(len(X_data_full))  # this scrambles the data each time
X_data_full = X_data_full[indices]
y_data_full = y_data_full[indices]



#
# The first nine are our test set - the rest are our training
#
X_test = X_data_full[0:9,0:4]              # the final testing data
X_train = X_data_full[9:,0:4]              # the training data

y_test = y_data_full[0:9]                  # the final testing outputs/labels (unknown)
y_train = y_data_full[9:]                  # the training outputs/labels (known)




# here is where you can re-scale/change column values...
# X_data[:,0] *= 100   # maybe the first column is worth 100x more!
# X_data[:,3] *= 100   # maybe the fourth column is worth 100x more!




#
# create a kNN model and tune its parameters (just k!)
#   here's where you'll loop to run 5-fold (or 10-fold cross validation)
#   and loop to see which value of n_neighbors works best (best cv testing-data score)
#

knn = KNeighborsClassifier(n_neighbors=7)   # 7 is the "k" in kNN


def cv_n_times(n):
    """function runs cross validation on the set n number of times"""
    train = 0
    test = 0
    for i in range(n):
        cv_data_train, cv_data_test, cv_target_train, cv_target_test =             cross_validation.train_test_split(X_train, y_train, test_size=0.25)
        knn.fit(cv_data_train, cv_target_train)
        train += knn.score(cv_data_train, cv_target_train)
        test += knn.score(cv_data_test, cv_target_test)
    #average fit score for training sets
    avgTrain = train/n
    #average fit score for test sets
    avgTest = test/n
    return avgTrain, avgTest

#10 fold cross validation
cv_n_times(10)
        

def pick_num_neighbors():
    """function when run, plots training and testing scores. It is easy to see from the graph which k to use. """
    klist = list(range(1,20))
    scoresTR = []
    scoresTE = []
    for i in klist:
        knn = KNeighborsClassifier(n_neighbors=i)
        knn.fit(cv_data_train, cv_target_train)
        scoresTR.append(knn.score(cv_data_train, cv_target_train))
        scoresTE.append(knn.score(cv_data_test, cv_target_test))
    plt.plot(klist, scoresTR, label = 'training scores')
    plt.plot(klist, scoresTE, label = 'test scores')
    plt.ylabel("Score Value")
    plt.xlabel("Number of Neighbors")
    plt.title('KNN Scores')
    plt.legend()
    plt.show()

pick_num_neighbors()


# In[176]:

#
# now, we train the model with ALL of the training data...  and predict the labels of the test set
#

X_data_full = df.iloc[:,0:4].values        # iloc == "integer locations" of rows/cols
y_data_full = df[ 'irisname' ].values      # individually addressable columns (by name)
y_test = y_data_full[0:9]                  # the final testing outputs/labels (unknown)
X_test = X_data_full[0:9,0:4]              # the final testing data

#
# we can scramble the remaining data
# 

X_train = X_data_full[9:,0:4]              # the training data        
y_train = y_data_full[9:]                  # the training outputs/labels (known)

indices = np.random.permutation(len(X_train))
X_train = X_train[indices]
y_train = y_train[indices]

# creating and training knn with 6 nearest neighbors
knn=KNeighborsClassifier(n_neighbors=6)
knn.fit(X_train, y_train) 


# 
# here is the output - for side-by-side comparison
#
def retransform(s):
    """ from number to string
          setosa <- 0
          versicolor <- 1
          virginica <- 2
    """
    d = { 0:'setosa', 1:'versicolor', 2:'virginica' }
    return d[s]

#creating and printing a dataframe for the inputs and predictions
names = list(map(retransform, knn.predict(X_test)))
output = df[['sepallen', 'sepalwid', 'petallen', 'petalwid' ]][0:9]
output['irisname'] = names
print(output)


"""
Comments and results:
  
  In the graph we see that k=6 is the smallest number of neibors with the largest score for both 
  training and test data.
  
  re-running the knn model yeilded the same results
  



The predicted labels of the first 9 irises (with "unknown" type):
 'versicolor',
 'virginica',
 'versicolor',
 'versicolor',
 'setosa',
 'setosa',
 'virginica',
 'versicolor',
 'setosa'.

"""



