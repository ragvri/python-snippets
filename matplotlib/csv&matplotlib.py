import matplotlib.pyplot as plt
from matplotlib.pyplot import style
import pandas as pd
import numpy as np

style.use('ggplot')

# could also use csv module
# x, y = np.loadtxt('sample.csv', unpack=True, delimiter=',')  # unpack as x and y
# numpy gives arrays instead of list

# print(x)
# print(y)

df = pd.read_csv('sample.csv', index_col=0)  # index is the x label and rest all are Y's
plt.plot(df)
plt.show()
