def intro():
    for i in range(5):  # here range is a generator. It is not a list. They are not loaded in memory.
        pass

    x = [i for i in range(5)]
    # same as
    y = []
    for i in range(5):
        y.append()

    # generator expression
    x = (i for i in range(5))  # does not store in memory as a list. It is a generator now
    print(x)  # gives a generator object
    # to work with a generator object like a range. We iterate over it like:
    for i in x:
        print(i)

        # it takes time to make a list as first everything needs to be in memory. Not for generator. However once a
        #   list is loaded, it is easier to work with it


input_list = [5, 6, 2, 10, 2, 5, 15, 20]


def div_by_five(num):
    return num % 5 == 0


xyz = (i for i in input_list if div_by_five(i))
for i in xyz:
    print(i)
# or we could also have done
[print(i) for i in xyz]  # so they are one liner for loops

[[print(i, ii) for ii in range(5)] for i in range(5)]
# same as . So backwards
for i in range(5):
    for ii in range(5):
        pass
    pass
