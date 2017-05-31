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
if __name__ == '__main__':
    for i in range(5):
        for ii in range(5):
            pass
        pass


# Everything that we can use "for foo in" is an iterable. eg list,string,dict,files Generators are iterators but
# you can iterate over them only once. Its because they do not store the values in memory, they generate them
#  on fly yield is a keyword like return except the function returns a generator
def create_generator():
    mylist = range(3)
    for i in mylist:
        yield i


my_generator = create_generator()
print(my_generator)  # generator object createGenerator at 0xb7555c34
for i in my_generator:
    print(i)
    # 1 ,2 ,3

# *************************************

"""when you call the function, the code you have written in the function body does not run. The function only returns
the generator object Then, your code will be run each time the for uses the generator.

 The first time the for calls
the generator object created from your function, it will run the code in your function from the beginning until it
hits yield, then it'll return the first value of the loop. Then, each other call will run the loop you have written
in the function one more time, and return the next value, until there is no value to return.

The generator is considered empty once the function runs but does not hit yield anymore. It can be because the loop had come to an end, or because you do not satisfy an "if/else" anymor
"""
