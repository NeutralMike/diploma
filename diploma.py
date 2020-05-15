from sklearn.linear_model import LinearRegression, ElasticNet, ElasticNetCV
from sklearn.ensemble import GradientBoostingRegressor
from sklearn.model_selection import train_test_split
import matplotlib.pyplot as plt

import pandas as pd

raw_data = pd.concat([
    pd.read_excel('data/1-500.xls', parse_dates=[['Дата', 'Время']]),
    pd.read_excel('data/501-1000.xls', parse_dates=[['Дата', 'Время']]),
    pd.read_excel('data/1001-1500.xls', parse_dates=[['Дата', 'Время']], decimal=','),
    pd.read_excel('data/1501-2000.xls', parse_dates=[['Дата', 'Время']], decimal=','),
    pd.read_excel('data/2001-2500.xls', parse_dates=[['Дата', 'Время']]),
    pd.read_excel('data/2501-3000.xls', parse_dates=[['Дата', 'Время']]),
    pd.read_excel('data/3001-3500.xls', parse_dates=[['Дата', 'Время']], decimal=','),
])
raw_data['Дата_Время'] = pd.to_numeric(raw_data['Дата_Время'])
features_of_y = {
    'Fг': ['Pвэ', 'Рпб', 'ИМГ', 'fдым', 'Pдэ', 'Рго'],
    'Fв': ['Pвэ', 'Рпб', 'Tвэ', 'ИМП', 'Tдк'],
    'СО': ['Tг', 'Pдэ', 'Рго', 'fдым', 'Дата_Время'],
    'О2к': ['Tг', 'Pдэ', 'Рго', 'fдым', 'Дата_Время'],
}
# print(X)
for y_col, x_cols_list in features_of_y.items():
    y = raw_data[y_col]
    X = raw_data[x_cols_list]
    X_train, X_test, y_train, y_test = train_test_split(X, y)
    regr = LinearRegression()
    regr.fit(X_train, y_train)
    elastic = ElasticNet()
    elastic.fit(X_train, y_train)
    elastic_cv = ElasticNetCV()
    elastic_cv.fit(X_train, y_train)
    boost_regr = GradientBoostingRegressor()
    boost_regr.fit(X_train, y_train)
    print('Prediction for \"', y_col, '\" :',
          '\n    Linear regression: ', regr.score(X_test, y_test),
          '\n    Linear regression with L1 and L2: ', elastic.score(X_test, y_test),
          '\n    Linear regression with L1 and L2 and cross-validation: ', elastic_cv.score(X_test, y_test),
          '\n    Gradient boosting: ', boost_regr.score(X_test, y_test))
    # y_pred = regr.predict(X_test)
    # for i in range(len(y_test)):
    #     print(y_pred[i], " ", list(y_test)[i])
    # print(regr.score(X_test, y_test))
    # y_pred = boost_regr.predict(X_test)
    # for i in range(len(y_test)):
    #     print(y_pred[i], " ", list(y_test)[i])
    # print(boost_regr.score(X_test, y_test))