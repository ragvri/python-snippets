import threading
from queue import Queue
import time

# a python program exits when only the daemon threads are left
# to make a thread daemon, thread.setDaemom(True)

count = 0
q = Queue(maxsize=0)  # maxsize=0 tells the max size can be infinite

''' Suppose for eg there is a function which continuosly updates the value of a variable count which was
    initially 0 every 1 second. You want to exit the program if the value of count >10. The function which updates
    count cannot be modified. So we take the value of count by the funciton and put in in a queue. We make
    a second function which gets the value of count from the queue and exits if count > 10 . We also make the first thread
    as a Daemon. So when the second thread ends, the program stops'''


def update_count():
    global count, q
    while True:
        count += 1
        q.put(count)
        time.sleep(1)


a = threading.Thread(name='first thread', target=update_count)
a.setDaemon(True)


def check_count():
    global count, q
    while True:
        if q.empty():
            continue
        else:
            value = q.get()
            if value > 10:
                print("The value of count in now greater than 10")
                return


b = threading.Thread(name='second thread', target=check_count)

a.start()
b.start()
