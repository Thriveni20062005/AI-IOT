# -*- coding: utf-8 -*-
"""Untitled2.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1wBUrPaHQd-Fyd_HxuJR1EgosKQduZRmp
"""

import pandas as pd
df = pd.read_csv('Data.csv')
# Step-1 We have to import the dataset to the colab notebook
import pandas as pd #pd is an instance of pandas
df=pd.read_csv('Data.csv')#df is a variable,read_csv is a predefined function from

type(df)

df

#step-2 grouping the input columns and output columns
X=df.iloc[:,0:-1]

X

Y=df.iloc[:,-1] #slicing the output column

Y

X=X.values

X # two dementional array

Y=Y.values

Y

#step-3:Handling missing data and NaN values
#scenario-1:
#scenario-2:
#scenario-3:

import numpy as np #
from sklearn.impute import SimpleImputer

imputer=SimpleImputer(missing_values=np.nan,strategy='mean')
imputer.fit(X[:,1:3])
X[:,1:3]=imputer.transform(X[:,1:3])

X

#step-4 handling catogorial data
#which converts the text data into numarical data
from sklearn.preprocessing import OneHotEncoder
from sklearn.compose import ColumnTransformer

#Alexa-0,0,1

ct=ColumnTransformer(transformers=[('encode',OneHotEncoder(),[0])],remainder='passthrough')

X=ct.fit_transform(X)

X

from sklearn.preprocessing import LabelEncoder
le=LabelEncoder()
Y=le.fit_transform(Y)

Y

#step-5: Split the data into training and testing data
from sklearn.model_selection import train_test_split   #model_selection
X_train,X_test,Y_train,Y_test=train_test_split(X,Y,test_size=0.2)

X_test

Y_train

Y_test

#step-6:frature scaling
from sklearn.preprocessing import StandardScaler
sc=StandardScaler()
X_train[:,3:]=sc.fit_transform(X_train[:,3:])
X_test[:,3:]=sc.fit_transform(X_test[:,3:])

X_train

X_test

#machine learning
#1.supervisioned learning -when we have label data,
# the model task are classification or prediction
#2.unspervisioned learning -unlabled data, model remembers the patterns
# we can perform prediction also.
#3.reinforcement learning-trail and error method,model learns from failure

#logistic regression algorithm=
#linear regression algorithm

#step-7:applying algorithm to the  training data for
from sklearn.linear_model import LogisticRegression
classifier=LogisticRegression()
classifier.fit(X_train,Y_train)

Y_pred=classifier.predict(X_test)

Y_pred