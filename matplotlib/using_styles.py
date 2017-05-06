# adding styles

import matplotlib.pyplot as plt
from matplotlib.pyplot import style

style.use('ggplot')  # a new style of graph

x = [5, 6, 7, 8]
y = [7, 3, 8, 3]
x2 = [3, 4, 5, 6]
y2 = [2, 3, 4, 5]

plt.plot(x, y)  # first is X axis and second is Y axis
plt.title('Epic chart')  # title of graph
plt.ylabel('Y axis')
plt.xlabel('X axis')
plt.show()

# x and y should have the same number

# can use your own styles as well
plt.plot(x, y, 'red',linewidth=5)
plt.plot(x2, y2, 'green')
plt.show()
