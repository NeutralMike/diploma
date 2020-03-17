import pandas as pd
import random

data_dict = {
    'a': [],
    'b': [],
    'x': [],
    'y': [],
}

for main_for_index in range(100):
    dots = []
    a = int((random.random() - 0.5) * 100 // 1)
    b = int((random.random() - 0.5) * 100 // 1)

    for a_for_index in range(100):
        varying_a = int((random.random() - 0.5) * 100 // 1)
        varying_b = int((random.random() - 0.5) * 100 // 1)

        for x_y_for_index in range(-100, 100):
            data_dict['a'].append(varying_a)
            data_dict['b'].append(b)
            data_dict['x'].append(x_y_for_index)
            data_dict['y'].append(varying_a * x_y_for_index ** 2 + b)

        for x_y_for_index in range(-100, 100):
            data_dict['a'].append(a)
            data_dict['b'].append(varying_b)
            data_dict['x'].append(x_y_for_index)
            data_dict['y'].append(a * x_y_for_index ** 2 + varying_b)



df = pd.DataFrame(data_dict)

df.to_csv('data.csv', index=False)

data = pd.read_csv('data.csv')
print(data)

