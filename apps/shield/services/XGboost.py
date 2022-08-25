
import pandas as pd
import numpy as np
import joblib
import random
import pickle
from django.conf import settings
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from xgboost import XGBClassifier
from sklearn.metrics import accuracy_score


def train_malicious_link_detection():

    """
        Dataset-Source: https://github.com/cozpii/Malicious-URL-detection
    """
    
    #data = pd.read_csv(settings.DATA_URL+"url_data.csv")
    data = pd.read_csv("apps/shield/data/xgb_url_data.csv")
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
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

    xgb = XGBClassifier(use_label_encoder =False,learning_rate=0.4,max_depth=7)

    #fit the model
    xgb.fit(X_train, y_train)
    #predicting the target value from the model for the samples
    y_test_xgb = xgb.predict(X_test)
    y_train_xgb = xgb.predict(X_train)
    model_score=xgb.score(X_test, y_test)
    print("\nScore : ", model_score)

    #pickle.dump(xgb, open("apps/shield/data/XGBoostClassifier.pickle.dat", "wb"))
    #pickle.dump(xgb, open("apps/shield/data/phishing.pkl", "wb"))

    malicious_url_xgb_model_dump = 'apps/shield/data/malicious_url_xgb.sav'
    joblib.dump(xgb, malicious_url_xgb_model_dump)
    print("\nTraining completed for for XGB")

def xgb_malicious_link_detection(test_link): # list of links

    # 1. Using Tokenizer
    vectorizer = TfidfVectorizer()

    # 2. initialize the vectorizer
    data = pd.read_csv("apps/shield/data/xgb_url_data.csv")
    url_list = list(data["url"])
    vectorizer = vectorizer.fit(url_list)

    # 3. Parse data
    test_data = vectorizer.transform(test_link)
    #print(test_data.shape)

    # 4. load the model from disk
    malicious_url_xgb_model = joblib.load("apps/shield/data/malicious_url_xgb.sav")

    # 5. Prediction from trained model
    result = malicious_url_xgb_model.predict(test_data)

    # 6. construct resultset
    resultset = {}
    for i in range(len(test_link)):
        resultset.update({test_link[i]: False if result[i] == 'good' else True })

    #return resultset
    print(resultset)
    
xgb_malicious_link_detection(["amazon.com", "amazon.in", "xxxx.yyy", "www.amezon.com", "www.ammazon.com"])
#train_malicious_link_detection()