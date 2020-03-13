import pandas as pd
import random

in_dict = {
    'a': [],
    'b': [],
    'dots': [],
}

for i in range(10000):
    dots = []
    a = int((random.random() - 0.5) * 1000)
    b = int((random.random() - 0.5) * 1000)

    in_dict['a'].append(a)
    in_dict['b'].append(b)

    for j in range(-100, 100):
        dots.append([j, a*j**2+b])

    in_dict['dots'].append(dots)

df = pd.DataFrame(in_dict)

df.to_csv('data.csv', index=False)

data = pd.read_csv('data.csv')
print(data)

