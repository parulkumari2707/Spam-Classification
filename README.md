Spam Message Classifier
===
This project uses a Naive Bayes classifier to classify SMS messages as spam or not.

Description
====
This project implements a spam message classifier using the Naive Bayes algorithm. It analyzes a dataset containing SMS messages labeled as spam or not spam and trains a classifier to predict whether a new message is spam or not.

Data Description
===
The dataset used for analysis contains SMS messages labeled as spam or not spam.

Tools and Libraries Used
===
+ NumPy
+ Pandas
+ Matplotlib
+ Scikit-learn
+ Chardet

Setup Instructions
===
**1. Clone the repository:**
```bash
git clone https://github.com/parulkumari2707/Spam-Classification.git
cd spam-message-classifier
```

**2. Install the required dependencies:**

``` bash
pip install numpy pandas matplotlib scikit-learn chardet
``` 

**3. Download the dataset file** (spam.csv) and place it in the project directory.

**4. Run the Python script:**
``` bash
python spam_classifier.py
```

Project Overview
==

1. Data Loading:
Load the dataset and detect the encoding using Chardet.

2. Data Preprocessing:
Select relevant columns and rename them.
Split the data into training and testing sets.

3. Feature Engineering:
Convert text data into numerical data using CountVectorizer.

4. Model Training:
Initialize and train the Naive Bayes classifier.

5. Model Evaluation:
Make predictions on the test set.
Evaluate the model's accuracy and create a confusion matrix.

6. Data Visualization:
Plot the distribution of labels (spam vs. not spam).
Plot the distribution of message lengths.

Conclusion
===
This project demonstrates the implementation of a simple spam message classifier using a Naive Bayes classifier in Scikit-learn.
