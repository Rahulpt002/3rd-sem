import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.metrics import confusion_matrix, accuracy_score, classification_report
from sklearn.naive_bayes import GaussianNB
from sklearn.datasets import load_iris

# Load dataset
x, y = load_iris(return_X_y=True)

# Split the dataset into training and test sets
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.40)

# Initialize the Gaussian Naive Bayes classifier
classifier = GaussianNB()

# Train the model
classifier.fit(x_train, y_train)

# Predict the test set results
y_pred = classifier.predict(x_test)

# Confusion matrix
result = confusion_matrix(y_test, y_pred)
print("Confusion Matrix")
print(result)

# Classification report
result2 = classification_report(y_test, y_pred)
print("Classification Report")
print(result2)

# Accuracy score
result3 = accuracy_score(y_test, y_pred)
print("Accuracy")
print(result3)