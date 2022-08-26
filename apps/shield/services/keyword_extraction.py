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

    # 1. Load model
    cv = pickle.load(open('apps/shield/data/vectorizer.pickle', 'rb'))
    keyword_model = pickle.load(open('apps/shield/data/spam_text.model', 'rb'))
    
    # 2. Prediction from trained model
    result = keyword_model.predict(cv.transform([email_text_content]))
    
    print(result)
    return True if result == 'spam' else False


#train_keyword_extraction()
#Content = "hi you won the lottery !!!! Congratulations ! FREE !!!"
#keyword_extraction(Content)