from sklearn.ensemble import GradientBoostingRegressor

import pandas as pd
import numpy as np
import time

train_data = pd.concat([
    pd.read_excel('data/1-500.xls', parse_dates=[['Дата', 'Время']]),
    pd.read_excel('data/501-1000.xls', parse_dates=[['Дата', 'Время']]),
    pd.read_excel('data/1001-1500.xls', parse_dates=[['Дата', 'Время']], decimal=','),
    pd.read_excel('data/1501-2000.xls', parse_dates=[['Дата', 'Время']], decimal=','),
    pd.read_excel('data/2001-2500.xls', parse_dates=[['Дата', 'Время']]),
]).sample(frac=1)
train_data['Дата_Время'] = pd.to_numeric(train_data['Дата_Время'])

predict_data = pd.concat([
    pd.read_excel('data/2501-3000.xls', parse_dates=[['Дата', 'Время']]),
    pd.read_excel('data/3001-3500.xls', parse_dates=[['Дата', 'Время']], decimal=','),
])
predict_data['Дата_Время'] = pd.to_numeric(predict_data['Дата_Время'])

gaz_X_train = train_data[['Pвэ', 'Рпб', 'ИМГ', 'fдым', 'Pдэ', 'Рго']]
gaz_y_train = train_data['Fг']
gaz_model = GradientBoostingRegressor()
gaz_model.fit(gaz_X_train, gaz_y_train)

water_X_train = train_data[['Pвэ', 'Рпб', 'Tвэ', 'ИМП', 'Tдк']]
water_y_train = train_data['Fв']
water_model = GradientBoostingRegressor()
water_model.fit(water_X_train, water_y_train)

print('среднее значение было бы :', (predict_data['Fг']/predict_data['Fв']).mean())

minimals = []
how_much_changed = []
for _, row in predict_data.iterrows():
    temp_row = row.copy()
    start_time = time.time()
    minimal = {'row': row, 'gaz/water': row['Fг']/row['Fв']}
    # print('Было бы:', minimal['gaz/water'])
    temp_row['ИМГ'] = 100.0
    temp_row['ИМП'] = 100.0
    # temp_row['Pвэ'] = 5.2
    # temp_row['fдым'] = 50
    # temp_row['Tдк'] = 500.
    # for pve in np.arange(2, 6.1, 0.1):
    #     temp_row['Pвэ'] = pve
    #     for img in range(0, 101, 5):
    #         temp_row['ИМГ'] = img
    # for imp in range(0, 101, 5):
    #     temp_row['ИМП'] = imp
    #     for f_smoke in range(20, 51):
    #         temp_row['fдым'] = f_smoke
    # for pde in range(-500, 1, 5):
    #     temp_row['Pдэ'] = pde
    #     for pgo in np.arange(0, 8.1, 0.1):
    #         temp_row['Рго'] = pgo
    # for tve in range(0, 181):
    #     temp_row['Tвэ'] = tve
    # for pve in np.arange(2, 6.1, 0.1):
    #     temp_row['Pвэ'] = pve
    #     for img in range(0, 101, 5):
    #         temp_row['ИМГ'] = img
    # for imp in range(0, 101, 5):
    #     temp_row['ИМП'] = imp
    #     for f_smoke in range(20, 51):
    #         temp_row['fдым'] = f_smoke
    # for pde in range(-500, 1, 5):
    #     temp_row['Pдэ'] = pde
    #     for pgo in np.arange(0, 8.1, 0.1):
    #         temp_row['Рго'] = pgo
    # for tve in range(0, 141, 5):
    #     temp_row['Tвэ'] = tve
    #     for tdk in range(50, 501, 5):
    #         temp_row['Tдк'] = tdk
    gaz_predict = gaz_model.predict(np.array(temp_row[['Pвэ', 'Рпб', 'ИМГ', 'fдым', 'Pдэ', 'Рго']]).reshape((1, -1)))[0]
    water_predict = water_model.predict(np.array(temp_row[['Pвэ', 'Рпб', 'Tвэ', 'ИМП', 'Tдк']]).reshape((1, -1)))[0]
    gaz_water = gaz_predict/water_predict
    if gaz_water < minimal['gaz/water']:
        minimal['gaz/water'] = gaz_water
        minimal['row'] = temp_row

    minimals.append(minimal['gaz/water'])
    if minimal['gaz/water'] != row['Fг']/row['Fв']:
        how_much_changed.append(1)
    else:
        how_much_changed.append(0)

    # print('При:\n',
    #       'Pвэ  ', row['Pвэ'], ' --> ', minimal['row']['Pвэ'], '\n',
    #       'ИМГ  ', row['ИМГ'], ' --> ', minimal['row']['ИМГ'], '\n',
    #       'ИМП  ', row['ИМП'], ' --> ', minimal['row']['ИМП'], '\n',
    #       'fдым  ', row['fдым'], ' --> ', minimal['row']['fдым'], '\n',
    #       'Pдэ  ', row['Pдэ'], ' --> ', minimal['row']['Pдэ'], '\n',
    #       'Рго  ', row['Рго'], ' --> ', minimal['row']['Рго'], '\n',
    #       'Tвэ  ', row['Tвэ'], ' --> ', minimal['row']['Tвэ'], '\n',
    #       'Tдк  ', row['Tдк'], ' --> ', minimal['row']['Tдк'], '\n',
    #       '\n Будет:', minimal['gaz/water'],
    #       '\n', time.time() - start_time)
print('среднее значение: ', np.array(minimals).mean())
print('изменено ', sum(how_much_changed), '/', len(how_much_changed))