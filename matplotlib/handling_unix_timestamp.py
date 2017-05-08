# unix timestamp is the number of seconds after jan 1st 1970

import datetime as dt
import time
import matplotlib.pyplot as plt
import matplotlib

x = []

# we first need a list of time as datetime objects
# for that we first get time in unix using time.time()
# and then convert it to datetime.datetime objects using dt.datetime.fromtimestamp(time.time())
# then we convert this list of dates to matplotlib time format using date2num
# finally we plot using plt.plot_date(dates,values)

for i in range(10):
    print(i)
    rand = time.time()
    date = dt.datetime.fromtimestamp(rand)
    x.append(date)
    time.sleep(5)
values = [i for i in range(10)]

dates = matplotlib.dates.date2num(x)
plt.plot_date(dates, values)
plt.show()
# time.time() gives the current unix time
