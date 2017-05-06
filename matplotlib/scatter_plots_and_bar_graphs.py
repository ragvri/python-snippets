import matplotlib.pyplot as plt
from matplotlib.pyplot import style

style.use('ggplot')

x = [1, 2, 3, 4]
y = [7, 3, 8, 3]
x2 = [5, 6, 7, 8]
y2 = [2, 3, 4, 5]

# for scatter plot use scatter instead of plot
plt.scatter(x, y, label='line 1', color='green')
plt.scatter(x2, y2, label='line two', color='yellow')
# giving same color :(
# to get color add color='red'
plt.show()

# for bar charts
plt.bar(x, y, color='green', align='center')# center aligns the bar on the its x label
plt.show()
