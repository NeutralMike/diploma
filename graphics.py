import matplotlib.pyplot as plt

import pandas as pd


raw_data = pd.read_csv('data.csv',)
graphics_count = 0

while True:
    try:
        print("How many graphics to show?\nEnter number from 1 to 100:")
        graphics_count = int(input())
        break
    except ValueError:
        pass
    except Exception:
        break

for i in range(0, graphics_count):

    x_data = raw_data['x'][i*201:(i+1)*201]
    y_data = raw_data['y'][i*201:(i+1)*201]

    _, ax = plt.subplots()

    ax.plot(x_data, y_data, color = '#539caf')

    ax.set_title("Graphic")
    ax.set_xlabel('X')
    ax.set_ylabel('Y')
    plt.show()
