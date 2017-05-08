import threading


#  threading allows us to create threads in python
# threads allows a program to run multiple operations concurently at the same process space

def first_thread():
    print("First thread")
    return


a = threading.Thread(name="first thread",
                     target=first_thread)  # name gives name to the thread, target tells the function to execute


def second_thread():
    print("second thread")
    return


b = threading.Thread(name='Second thread', target=second_thread)

a.start()  # starts the thread
b.start()
