"""## Importing the libraries"""
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import pickle

"""## Importing the dataset"""
dataset = pd.read_csv('breast_cancer.csv')
X = dataset.iloc[:, 1:-1].values  # Independent variable
y = dataset.iloc[:, -1].values  # Dependent variable

"""## Splitting the dataset into the Training set and Test set"""
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=0)

"""## Training the Simple Linear Regression model on the Training set"""
from sklearn.ensemble import RandomForestClassifier
classifier = RandomForestClassifier(n_estimators=100, random_state=0)
classifier.fit(X_train, y_train)

# Saving model to disk
pickle.dump(classifier, open('model.pkl', 'wb'))

# Loading model to compare the results (read)
model = pickle.load(open('model.pkl', 'rb'))
