from sklearn.model_selection import train_test_split
from sklearn.ensemble import GradientBoostingRegressor

import pandas as pd
import numpy as np

raw_data = pd.read_csv('data/data.csv', )
X = raw_data[['a', 'b', 'x']]
y = raw_data['y']
X_train, X_test, y_train, y_test = train_test_split(X, y)
clf = GradientBoostingRegressor(n_estimators=100)
clf.fit(X_train, y_train)
print("Score for gradient boosting: ", clf.score(X_test, y_test))

scores = []

for i in range(-100, 101):
    X = raw_data[raw_data['x'] == i][['a', 'b']]
    y = raw_data[raw_data['x'] == i]['y']
    X_train, X_test, y_train, y_test = train_test_split(X, y)
    clf = GradientBoostingRegressor(n_estimators=100)
    clf.fit(X_train, y_train)
    scores.append(clf.score(X_test, y_test))

print("Average score of boosting for each X:", np.mean(scores))
