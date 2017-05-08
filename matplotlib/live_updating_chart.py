import matplotlib.pyplot as plt
import matplotlib.animation as animation
from matplotlib import style
import csv

style.use('fivethirtyeight')

fig = plt.figure()  # if the figure needs to be modified use this


def animate(i):
    with open('sample.csv') as csv_file:
        readcsv = csv.reader(csv_file, delimiter=',')
        xs = []
        ys = []
        for row in readcsv:
            if len(row) > 1:
                x, y = row
                xs.append(x)
                ys.append(y)
        fig.clear()
        plt.plot(xs, ys)


ani = animation.FuncAnimation(fig, animate, interval=1000)  # interval in ms, where to animate , which function to call
# so every 1 second graph will update

plt.show()
