import pandas as pd
import numpy as np
import random

data_dict = {
    'a': [],
    'b': [],
    'x': [],
    'y': [],
}

for main_for_index in range(100):
    a = int((random.random() - 0.5) * 1000)
    b = int((random.random() - 0.5) * 1000)

    for x_for_index in range(-100, 101):
        data_dict['a'].append(a)
        data_dict['b'].append(b)
        data_dict['x'].append(x_for_index)
        data_dict['y'].append(a*(x_for_index+b)**2)

df = pd.DataFrame(data_dict)

df.to_csv('data.csv', index=False)

data = pd.read_csv('data/data.csv')
print(data)

