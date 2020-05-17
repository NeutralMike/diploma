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

real_mean = (predict_data['Fг']/predict_data['Fв']).mean()
features_with_max_min = {
    'ИМП' : range(0, 101, 5),
    'ИМГ' : range(0, 101, 5),
    'Pвэ': np.arange(2, 6.1, 0.1),
    'fдым' : range(20, 51),
    'Pдэ' : range(-500, 1, 5),
    'Рго' : np.arange(0, 8.1, 0.1),
    'Tвэ' : range(0, 181),
    'Tдк' : range(50, 501, 5),
}

print('среднее значение было бы :', real_mean)

for feature_name, feature_range in features_with_max_min.items():
    start_time = time.time()
    minimals = []
    new_values = []
    how_much_changed = 0
    not_touched_values = []
    for _, row in predict_data.iterrows():
        temp_row = row.copy()
        minimal = {'row': row, 'gaz/water': row['Fг'] / row['Fв'], 'new_value': 0}
        for feature_value in feature_range:
            temp_row[feature_name] = feature_value
            gaz_predict = gaz_model.predict(np.array(temp_row[['Pвэ', 'Рпб', 'ИМГ', 'fдым', 'Pдэ', 'Рго']]).reshape((1, -1)))[0]
            water_predict = water_model.predict(np.array(temp_row[['Pвэ', 'Рпб', 'Tвэ', 'ИМП', 'Tдк']]).reshape((1, -1)))[0]
            gaz_water = gaz_predict/water_predict
            if gaz_water < minimal['gaz/water']:
                minimal['gaz/water'] = gaz_water
                minimal['row'] = temp_row
                minimal['new_value'] = temp_row[feature_name]

        minimals.append(minimal['gaz/water'])
        if minimal['gaz/water'] != row['Fг'] / row['Fв']:
            how_much_changed += 1
            new_values.append(minimal['row'][feature_name])
        else:
            not_touched_values.append(row[feature_name])

    print('{0} уменьшило отношение на {1:.2f}% ( {2} --> {3}).\n'
          '    Изменило {4}/1000.\n'
          '    Среднее новое значение для измненных строк {5}\n'
          '    Среднее значение неизмененных строк {6}\n'
          '    Время вычисления: {7}\n'.format(
            feature_name, 100 * ((real_mean - np.mean(minimals)) / real_mean), real_mean, np.mean(minimals),
            how_much_changed,
            np.mean(new_values),
            np.mean(not_touched_values),
            time.time() - start_time,
            ))
