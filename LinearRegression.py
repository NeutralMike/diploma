from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import explained_variance_score

import pandas as pd

raw_data = pd.read_csv('data.csv',)
X = raw_data[['a', 'b', 'x']]
y = raw_data['y']
X_train, X_test, y_train, y_test = train_test_split(X, y)
lr = LinearRegression()
lr.fit(X_train, y_train)
print(explained_variance_score(y_test, lr.predict(X_test)))
