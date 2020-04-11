from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import explained_variance_score
from sklearn.ensemble import GradientBoostingRegressor

import pandas as pd
import numpy as np

raw_data = pd.read_csv('data.csv',)
scores = []

for i in range(-100, 101):
    X = raw_data[raw_data['x'] == i][['a', 'b']]
    y = raw_data[raw_data['x'] == i]['y']
    X_train, X_test, y_train, y_test = train_test_split(X, y)
    lr = LinearRegression()
    lr.fit(X_train, y_train)
    scores.append(explained_variance_score(y_test, lr.predict(X_test)))

print(np.mean(scores))
