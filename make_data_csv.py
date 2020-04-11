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
    a = int((random.random() - 0.5) * 100)
    b = int((random.random() - 0.5) * 100)

    for x_for_index in range(-100, 101):
        data_dict['a'].append(a)
        data_dict['b'].append(b)
        data_dict['x'].append(x_for_index)
        data_dict['y'].append(a/(1+abs(np.sin(x_for_index**2) + np.sqrt(abs(b**3)))))

df = pd.DataFrame(data_dict)

df.to_csv('data.csv', index=False)

data = pd.read_csv('data.csv')
print(data)

