"""
main objective of numpy is to create a homogenous array. The dimensions of array is called axes.
len(axes) = rank

attributes:
ndarray.dim -> gives the dimension or rank of the array
ndarray.shape -> gives the [row,col[
ndarray.dtype -> gives the type of data. eg np.int32, np.float64

"""

import numpy as np

""" 1) Attributes"""
a = np.arange(15).reshape(3, 5)
# a
# array([[ 0,  1,  2,  3,  4],
#        [ 5,  6,  7,  8,  9],
#        [10, 11, 12, 13, 14]])
print(a.shape)
# (3,5)
print(a.ndim)
# 2
print(a.dtype.name)
# 'int64'

""" 2) Basic Creation and Usage"""
# we can create an array from a regular python list using array
a = np.array([2, 3, 4])  # creates a 1*3 array

b = np.array([(1, 2, 3), (4, 5, 6)])
print(b)
# b
# array([[ 1.5,  2. ,  3. ],
#        [ 4. ,  5. ,  6. ]])

# type of array can be specified while creation
c = np.array([1, 2, ], [3, 4], dtype=complex)
# c
# array([[ 1.+0.j,  2.+0.j],
#        [ 3.+0.j,  4.+0.j]])

a = np.zeros((3, 4))
# array([[ 0.,  0.,  0.,  0.],
#        [ 0.,  0.,  0.,  0.],
#        [ 0.,  0.,  0.,  0.]])
a = np.ones((2, 3), dtype=np.int16)

d = np.arange(10, 30, 5)  # arange works similiar to range. It accepts float unlike range
# array([10, 15, 20, 25])

e = np.linspace(0, 2, 9)  # tells that we need 9 equispaced numbers between 0 and 2
# array([ 0.  ,  0.25,  0.5 ,  0.75,  1.  ,  1.25,  1.5 ,  1.75,  2.  ])

# If an array is too large to be printed, NumPy automatically skips the central part of the array and only prints the
#  corners:
print(np.arange(1000))
# [   0    1    2 ..., 9997 9998 9999]

"""" 3) Arithmatic operations"""
# arithmatic operations on arrays apply element wise
a = np.array([1, 2, 3, 4])
b = np.arange(4)
print(a - b)
# array([20, 29, 38, 47])
c = np.dot(a, b)  # matrix multiplication of a and b

a = np.random.random((2, 3))  # creates a random array 2*3
a.sum()  # gives the sum of all elements
a.max()  # gives the max element

a = np.arange(12).reshape((3, 4))
a.sum(axis=0)  # gives rowwise sum
# array([12, 15, 18, 21])

""" 4)Indexing , Slicing and Iterating"""
a = np.arange(10) ** 3
# array([  0,   1,   8,  27,  64, 125, 216, 343, 512, 729])
a[2:5]
# array([ 8, 27, 64])
a[:6:2] = -1000  # from 0 to 6, change every 2nd element to -1000
# array([-1000,     1, -1000,    27, -1000,   125,   216,   343,   512,   729])
a.ravel()  # returns a flattened array
a.reshape(3, -1)  # means we want 3 rows and don't care about col. So col calculated automatically

""" 4) Linear Algebra"""
a = np.array([[1, 2], [3, 4]])
a.transpose()  # transposes a
np.linalg.inv(a)  # gives the inverse of a

