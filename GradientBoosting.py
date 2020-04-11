from sklearn.model_selection import train_test_split
from sklearn.ensemble import GradientBoostingRegressor

import pandas as pd

raw_data = pd.read_csv('data.csv', )
X = raw_data[['a', 'b', 'x']]
y = raw_data['y']
X_train, X_test, y_train, y_test = train_test_split(X, y)
clf = GradientBoostingRegressor(n_estimators=500)
clf.fit(X_train, y_train)
print(clf.score(X_test, y_test))
