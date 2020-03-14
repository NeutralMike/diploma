import pandas as pd
import random

data_dict = {
    'a': [],
    'b': [],
    'x': [],
    'y': [],
}

for i in range(10000):
    dots = []
    a = int((random.random() - 0.5) * 100 // 1)
    b = int((random.random() - 0.5) * 100 // 1)

    for j in range(-100, 100):
        data_dict['a'].append(a)
        data_dict['b'].append(b)
        data_dict['x'].append(j)
        data_dict['y'].append(a * j ** 2 + b)


df = pd.DataFrame(data_dict)

df.to_csv('data.csv', index=False)

data = pd.read_csv('data.csv')
print(data)

