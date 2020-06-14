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
])[1000:1100]


x_data = (raw_data['Дата_Время'] - raw_data['Дата_Время'][0]).astype('timedelta64[m]')
_, ax = plt.subplots()

ax.plot(x_data, raw_data['Fг']/raw_data['Fв'], label='Fг/Fв')
ax.plot(x_data, raw_data['ИМП'], label='ИМП')
ax.plot(x_data, raw_data['ИМГ'], label='ИМГ')

ax.set_title("Зависимость Fг/Fв от ИМП и ИМГ")
ax.set_xlabel("Время (в минутах)")
ax.legend()
plt.show()
