from sklearn.linear_model import LinearRegression
from sklearn.ensemble import GradientBoostingRegressor
from sklearn.model_selection import train_test_split

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
x_cols_list = ['Tвв', 'Fв', 'ИМП', 'Lб', 'Рпб', 'Fп', 'Тнв', 'fвент', 'ИМВ', 'Рвл', 'Рвп', 'Fг', 'Tг', 'ИМГ', 'Pгг', 'Ргл', 'Ргп', 'Ртк', 'СО', 'fдым', 'ИМТ']
y_cols_list = ['Tвэ', 'Pвэ', 'О2к', 'О2э', 'Рдк', 'Tдк', 'Тдэ', 'Pдэ']
X = raw_data[x_cols_list]
# print(X)
for i in y_cols_list:
    y = raw_data[i]
    X_train, X_test, y_train, y_test = train_test_split(X, y, shuffle=False)
    regr = LinearRegression()
    regr.fit(X_train, y_train)
    boost_regr = GradientBoostingRegressor()
    boost_regr.fit(X_train, y_train)
    print('Prediction for \"', i, '\" :\n    Linear regression: ', regr.score(X_test, y_test), '\n    Gradient boosting: ', boost_regr.score(X_test, y_test))
    # y_pred = regr.predict(X_test)
    # for i in range(len(y_test)):
    #     print(y_pred[i], " ", list(y_test)[i])
    # print(regr.score(X_test, y_test))
    # y_pred = boost_regr.predict(X_test)
    # for i in range(len(y_test)):
    #     print(y_pred[i], " ", list(y_test)[i])
    # print(boost_regr.score(X_test, y_test))