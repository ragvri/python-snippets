# 1) python functions are actually objects
def shout(word='yes'):
    return word.capitalize() + '!'


print(shout())
# outputs :'Yes!'

# As an object you can assign a function to a variable like any other object
scream = shout
# We are not putting any parenthesis as we don't want to call the function.

print(scream())
# outputs :'Yes!'

# More than that, it means you can remove the old name 'shout',
# and the function will still be accessible from 'scream'

del shout
try:
    print(shout())
except Exception as e:
    print(e)
    # outputs: "name 'shout' is not defined"

print(scream())


# outputs: 'Yes!'

# ***************************************************

# 2) In python functions can be defined inside other functinos

def talk():
    # you can define a function on the fly in talk
    def whisper(word='yes'):
        return word.lower()

    # and use it right away
    print(whisper())


# You call "talk", that defines "whisper" EVERY TIME you call it, then
# "whisper" is called in "talk".
talk()
# outputs:
# "yes..."

# But "whisper" DOES NOT EXIST outside "talk":

try:
    print(whisper())
except Exception as e:
    print(e)


# outputs : "name 'whisper' is not defined"*
# Python's functions are objects

# *****************************************************

# So function can be assigned to a variable and function can be defined in another function
# this means that a function can return another function

def getTalk(kind="shout"):
    # We define functions on the fly
    def shout(word="yes"):
        return word.capitalize() + "!"

    def whisper(word="yes"):
        return word.lower() + "..."

    # Then we return one of them
    if kind == "shout":
        # We don't use "()", we are not calling the function,
        # we are returning the function object
        return shout
    else:
        return whisper


# How do you use this strange beast?

# Get the function and assign it to a variable
talk = getTalk()

# You can see that "talk" is here a function object:
print(talk)
# outputs : <function shout at 0xb7ea817c>

# The object is the one returned by the function:
print(talk())
# outputs : Yes!

# And you can even use it directly if you feel wild:
print(getTalk("whisper")())


# outputs : yes...

# ******************************************************

# So if you can return a function, you can pass one as a parameter
def doSomethingBefore(func):
    print("I do something before then I call the function you gave me")
    print(func())


doSomethingBefore(scream)


# outputs:
# I do something before then I call the function you gave me
# Yes!

# ********************************************************************'

# A decorator is a function that expects ANOTHER function as parameter
def my_shiny_new_decorator(a_function_to_decorate):
    # Inside, the decorator defines a function on the fly: the wrapper.
    # This function is going to be wrapped around the original function
    # so it can execute code before and after it.
    def the_wrapper_around_the_original_function():
        # Put here the code you want to be executed BEFORE the original function is called
        print("Before the function runs")

        # Call the function here (using parentheses)
        a_function_to_decorate()

        # Put here the code you want to be executed AFTER the original function is called
        print("After the function runs")

    # At this point, "a_function_to_decorate" HAS NEVER BEEN EXECUTED.
    # We return the wrapper function we have just created.
    # The wrapper contains the function and the code to execute before and after. It’s ready to use!
    return the_wrapper_around_the_original_function


# Now imagine you create a function you don't want to ever touch again.
def a_stand_alone_function():
    print("I am a stand alone function, don't you dare modify me")


a_stand_alone_function()
# outputs: I am a stand alone function, don't you dare modify me

# Well, you can decorate it to extend its behavior.
# Just pass it to the decorator, it will wrap it dynamically in
# any code you want and return you a new function ready to be used:

a_stand_alone_function_decorated = my_shiny_new_decorator(a_stand_alone_function)
a_stand_alone_function_decorated()
# outputs:
# Before the function runs
# I am a stand alone function, don't you dare modify me
# After the function runs

# Now, you probably want that every time you call a_stand_alone_function, a_stand_alone_function_decorated is called
# instead
a_stand_alone_function = my_shiny_new_decorator(a_stand_alone_function)
a_stand_alone_function()


# outputs:
# Before the function runs
# I am a stand alone function, don't you dare modify me
# After the function runs

# That’s EXACTLY what decorators do!

@my_shiny_new_decorator
def another_stand_alone_function():
    print("Leave me alone")


another_stand_alone_function()
# outputs:
# Before the function runs
# Leave me alone
# After the function runs
