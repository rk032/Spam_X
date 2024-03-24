# SPAM_X

## Introduction
This project focuses on classifying emails as either spam or ham (non-spam) utilizing the Naive Bayes algorithm. The dataset utilized for training and testing purposes was sourced from Kaggle.

## Dataset Preprocessing
Prior to applying the Naive Bayes algorithm, various preprocessing steps were conducted to clean and prepare the dataset:

### 1. Removing Null Values
Any rows containing null values were eliminated from the dataset to maintain data integrity.

### 2. Removing Duplicates
Duplicate entries in the dataset were removed to mitigate bias and redundancy during the training process.

### 3. Removing Unwanted Columns
Columns deemed irrelevant to the classification task were discarded from the dataset to streamline dimensionality.

### Text Processing
The text data underwent several preprocessing steps to standardize the format and render it suitable for analysis:

#### i) Removing Punctuation
Punctuation marks such as periods, commas, and exclamation points were stripped from the text data as they typically do not contribute to the classification task.

#### ii) Converting to Lower Case
All text data was converted to lowercase to ensure uniformity in word representations and avoid duplication of words due to case sensitivity.

#### iii) Removing Digits
Numeric digits were removed from the text data as they are typically not indicative of spam or ham emails.

#### iv) Removing Stopwords
Stopwords, such as 'and', 'the', and 'is', were eliminated from the text data as they do not convey significant meaning for the classification task.

#### v) Lemmatization
Lemmatization was employed to reduce words to their base or root form, aiding in standardizing the vocabulary and enhancing classification accuracy.

## TF-IDF Vectorization
TF-IDF (Term Frequency-Inverse Document Frequency) vectorization was applied to convert the text data into numerical features. This technique represents each document as a vector of word frequencies weighted by their importance in the corpus. It helps capture the significance of words in distinguishing between spam and ham emails.

## Naive Bayes Classification
The Naive Bayes algorithm was selected for this classification task due to its efficacy in handling text data. Naive Bayes assumes that features are conditionally independent given the class, making it particularly suitable for text classification tasks where the presence of one word may not necessarily affect the presence of another.

## Front End Development with Flask
A front-end interface was developed using Flask to interact with the Naive Bayes classification model. Flask routes were defined to handle user inputs, pass them to the classification model, and display the results.

## Image Gallery
![Alt Text](https://github.com/ParthaSarathi-23/SPAM_X/blob/main/Img-1.png?raw=true)

