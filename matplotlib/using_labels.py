# adding labels to show in legend

import matplotlib.pyplot as plt

x = [5, 6, 7, 8]
y = [7, 3, 8, 3]
x2 = [3, 4, 5, 6]
y2 = [2, 3, 4, 5]

# x and y should have the same number

# can use your own styles as well
plt.plot(x, y, 'red', linewidth=5, label='line 1')
plt.plot(x2, y2, 'green', linewidth=2, label='line two')
plt.legend()  # shows the legend of labels
plt.show()
