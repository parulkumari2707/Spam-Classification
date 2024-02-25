# -*- coding: utf-8 -*-
"""Spam_classification_Naive_Bayes.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1siX_ojIWG5K2CRXQ-C7sy37Jj-h992kU
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.metrics import accuracy_score, confusion_matrix

!pip install chardet

import chardet

with open('/content/drive/MyDrive/spam.csv', 'rb') as f:
    encoding = chardet.detect(f.read())['encoding']

data = pd.read_csv('/content/drive/MyDrive/spam.csv',encoding=encoding)

data.head()

data.info()

data = data[['v1', 'v2']]
data.columns = ['label', 'text']

# Splitting the data into train and test sets
X_train, X_test, y_train, y_test = train_test_split(data['text'], data['label'], test_size=0.2, random_state=42)

# Convert text data into numerical data using CountVectorizer
vectorizer = CountVectorizer()
X_train = vectorizer.fit_transform(X_train)
X_test = vectorizer.transform(X_test)

# Initialize and train the Naive Bayes classifier
nb_classifier = MultinomialNB()
nb_classifier.fit(X_train, y_train)

# Make predictions on the test set
y_pred = nb_classifier.predict(X_test)

# Evaluate the model
accuracy = accuracy_score(y_test, y_pred)
conf_matrix = confusion_matrix(y_test, y_pred)

print("Accuracy:", accuracy)
print("Confusion Matrix:\n", conf_matrix)

# Plotting the distribution of labels
plt.figure(figsize=(6, 4))
data['label'].value_counts().plot(kind='bar', color=['blue', 'orange'])
plt.title('Distribution of Labels')
plt.xlabel('Label')
plt.ylabel('Count')
plt.xticks(rotation=0)
plt.show()

# Plotting the distribution of message lengths
data['message_length'] = data['text'].apply(len)
plt.figure(figsize=(6,4))
data['message_length'].plot(kind='hist', bins=50, color='green')
plt.title('Distribution of Message Lengths')
plt.xlabel('Message Length')
plt.ylabel('Frequency')
plt.show()

