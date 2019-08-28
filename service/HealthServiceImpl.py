from sklearn import preprocessing
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression

import logging as logger


class HealthServiceImpl:

    def predict(self,x):
        logger.info("Starting laptop compaire method....")

        dataset = pd.read_csv('C:/Users/Sachith/Desktop/My ML models/CSV Files/Patient predict.csv')
        # separate the data from the target attributes
        X = dataset.iloc[:, :-1].values
        y = dataset.iloc[:, 1].values.reshape(-1, 2)
        # normalize the data attributes
        # normalized_X = preprocessing.normalize(X)
        normalized_Y = preprocessing.normalize(y)

        new_Y = normalized_Y.reshape(-1)

        X_train, X_test, y_train, y_test = train_test_split(X, new_Y, test_size=1 / 3, random_state=10)
        regressor = LinearRegression()
        regressor.fit(X_train, y_train)

        y_pred = regressor.predict([[x]])
        ans = y_pred * (403 - 8) + 8
        print(ans)
        return ans;