
import pandas as pd
import numpy as np
import joblib
import random
from django.conf import settings
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split

def train_malicious_link_detection():

    """
        Dataset-Source: https://www.kaggle.com/datasets/sid321axn/malicious-urls-dataset + https://github.com/cozpii/Malicious-URL-detection 
    """
    
    #data = pd.read_csv(settings.DATA_URL+"url_data.csv")
    data = pd.read_csv("apps/shield/data/url_data.csv")
    #data.head()

    # Labels
    y = data["label"]

    # Features
    url_list = list(data["url"])

    # Using Tokenizer
    vectorizer = TfidfVectorizer()

    # Store vectors into X variable as Our XFeatures
    vectorizer = vectorizer.fit(url_list)
    X = vectorizer.transform(data["url"])
    #print(X.shape)
    
    # Split into training and testing dataset 80:20 ratio
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    # Model Building using logistic regression
    logit = LogisticRegression()
    logit.fit(X_train, y_train)

    # Accuracy of Our Model
    print("Accuracy of our model is: ",logit.score(X_test, y_test))
    
    # save the model to disk
    malicious_url_model_dump = 'apps/shield/data/malicious_url_model.sav'
    joblib.dump(logit, malicious_url_model_dump)

    print("\nTraining completed for ")


def malicious_link_detection(test_link): # list of links

    # 1. Using Tokenizer
    vectorizer = TfidfVectorizer()

    # 2. initialize the vectorizer
    data = pd.read_csv("apps/shield/data/url_data.csv")
    url_list = list(data["url"])
    vectorizer = vectorizer.fit(url_list)

    # 3. Parse data
    test_data = vectorizer.transform(test_link)
    #print(test_data.shape)

    # 4. load the model from disk
    malicious_url_model = joblib.load("apps/shield/data/malicious_url_model.sav")

    # 5. Prediction from trained model
    result = malicious_url_model.predict(test_data)

    # 6. construct resultset
    resultset = {}
    for i in range(len(test_link)):
        resultset.update({test_link[i]: False if result[i] == 0 else True })

    return resultset    # {'amazon.com': 'good', 'mitaoe.ac.in': 'good', 'xxxx.yyy': 'bad'}
    
#malicious_link_detection(["amazon.com", "mitaoe.ac.in", "xxxx.yyy", "www.amezon.com", "www.ammazon.com"])
#train_malicious_link_detection()