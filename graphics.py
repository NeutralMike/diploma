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
raw_data['Дата_Время'] = pd.to_numeric(raw_data['Дата_Время'])

x_data = range(0, len(raw_data))

_, ax = plt.subplots()

ax.plot(x_data, raw_data['Fг']/raw_data['Fв'], label='Fг/Fв')
ax.plot(x_data, raw_data['ИМП'], label='ИМП')
ax.plot(x_data, raw_data['ИМГ'], label='ИМГ')

ax.set_title("Graphic")
ax.legend()
plt.show()
