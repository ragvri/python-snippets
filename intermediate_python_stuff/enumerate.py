example = ['left', 'right', 'up', 'down']

for i in range(len(example)):
    print(i, example[i])
# use instead

for i, j in enumerate(example):  # gives the index and value, better to use in place of len
    print(i, j)
