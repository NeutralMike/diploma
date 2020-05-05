from sklearn.linear_model import LinearRegression, ElasticNet, ElasticNetCV
from sklearn.ensemble import GradientBoostingRegressor
from sklearn.model_selection import train_test_split
import matplotlib.pyplot as plt

import pandas as pd

raw_data = pd.concat([
    pd.read_excel('data/1-500.xls', parse_dates=[['Дата', 'Время']], index_col='Дата_Время'),
    pd.read_excel('data/501-1000.xls', parse_dates=[['Дата', 'Время']], index_col='Дата_Время'),
    pd.read_excel('data/1001-1500.xls', parse_dates=[['Дата', 'Время']], index_col='Дата_Время', decimal=','),
    pd.read_excel('data/1501-2000.xls', parse_dates=[['Дата', 'Время']], index_col='Дата_Время', decimal=','),
    pd.read_excel('data/2001-2500.xls', parse_dates=[['Дата', 'Время']], index_col='Дата_Время'),
    pd.read_excel('data/2501-3000.xls', parse_dates=[['Дата', 'Время']], index_col='Дата_Время'),
    pd.read_excel('data/3001-3500.xls', parse_dates=[['Дата', 'Время']], index_col='Дата_Время', decimal=','),
])
x_cols_list = ['Tвв', 'Tвэ', 'Fв', 'Pвэ', 'ИМП', 'Lб', 'Рпб', 'Fп', 'Тнв', 'fвент', 'ИМВ', 'Рвл', 'Рвп', 'Fг', 'Tг', 'ИМГ', 'Pгг', 'Ргл', 'Ргп', 'Ртк', 'СО', 'О2э', 'Тдэ', 'fдым', 'ИМТ', 'Pдэ']
y_cols_list = ['О2к', 'Рдк', 'Tдк']
X = raw_data[x_cols_list]
# print(X)
for i in y_cols_list:
    y = raw_data[i]
    X_train, X_test, y_train, y_test = train_test_split(X, y)
    regr = LinearRegression()
    regr.fit(X_train, y_train)
    elastic = ElasticNet()
    elastic.fit(X_train, y_train)
    elastic_cv = ElasticNetCV()
    elastic_cv.fit(X_train, y_train)
    boost_regr = GradientBoostingRegressor()
    boost_regr.fit(X_train, y_train)
    print('Prediction for \"', i, '\" :',
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