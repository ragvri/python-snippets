# pickle is used to save python objects eg variables, classes, objects

import pickle

# let the variable to be saved be a
a = [1, 2, 3, 3, 4, 4, 55, 5, 7]

f = open('save_a.pickle', 'wb')
pickle.dump(a, f)
f.close()

# now to load the variable from the pickle created
g = open('save_a.pickle', 'rb')
b = pickle.load(g)
print(g)
