import email
import pandas as pd
import numpy as np
import joblib
import random
import pickle
from django.conf import settings
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB , GaussianNB
from sklearn import svm
from sklearn.model_selection import GridSearchCV

SPAM_DICTIONARY = [
                    "lottery", "free", "win", "jumbo offer", "free offer", "offer", "100% off", "exclusive offer"
                    "exclusive offer", "hurry now", "kill you", "fuck you", "bitch", "won free", "win free",
                    "win exciting", "exotic collection", "exclusive prize", "fuck", "fucker", "sex", "sexy", ""
                    "congrats", "!!!!", "!!!", "!!", "win exciting prize", "100 % discount", "50% discount", "click here",
                    "chance to win", "exciting prize", "Grand Prize", "won $", "won Rs", "win $", "claim your prize", "claim now",
                    "you’ve won the $"
                ]

def train_keyword_extraction():

    data_frame = pd.read_csv ("apps/shield/data/spam_text.csv")

    x = data_frame['EmailTextBody']
    y = data_frame['Label']
    X_train, X_test, y_train, y_test = train_test_split(x, y, test_size=0.1, random_state=2)

    cv = CountVectorizer()
    features = cv.fit_transform(X_train)
    tuned_parameter={'C':[1,10,100,1000]}

    keyword_model = GridSearchCV(svm.SVC(), param_grid = tuned_parameter).fit(features, y_train)
    #model = svm.SVC()

    vec_file = 'apps/shield/data/vectorizer.pickle'     # vector file
    pickle.dump(cv, open(vec_file, 'wb'))
    keyword_model_file = 'apps/shield/data/spam_text.model'     # model file
    pickle.dump(keyword_model, open(keyword_model_file, 'wb'))
    print("\nTraining cycle completed for spam_text model.")


def keyword_extraction(email_text_content):

    match_count = 0
    for spam_word in SPAM_DICTIONARY:
        if spam_word in email_text_content :
            result = True
            match_count += 1
    else:
        # 1. Load model
        cv = pickle.load(open('apps/shield/data/vectorizer.pickle', 'rb'))
        keyword_model = pickle.load(open('apps/shield/data/spam_text.model', 'rb'))
        
        # 2. Prediction from trained model
        result = True if keyword_model.predict(cv.transform([email_text_content])) == 'spam' else False
    
    spam_percent = match_count / len(email_text_content) * 100
    
    return result, spam_percent


#train_keyword_extraction()
#Content = "hi you won the lottery !!!! Congratulations ! FREE !!!"
#keyword_extraction(Content)