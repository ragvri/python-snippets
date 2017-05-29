"""
timeit measures time to run a snippet.
Better than:
start = time.time()
total_time = time.time()-start. Because it is not precise
"""

import timeit

print(timeit.timeit('1+3', number=500000))  # will print the time taken to get 1+3 5000000 times

input_list = range(100)


def div_by_five(num):
    return num % 5 == 0


xyz = (i for i in input_list if div_by_five(i))

print(timeit.timeit("""
input_list = range(100)


def div_by_five(num):
    return num % 5 == 0


xyz = (i for i in input_list if div_by_five(i))


""", number=50))
