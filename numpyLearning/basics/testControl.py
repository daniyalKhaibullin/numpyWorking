import numpy as np

"""
Basics of numpy
Arrays, multi-dimensional Arrays
Universal functions
and Slicing of the arrays
"""

#arrays in vanilla python
array0 = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
print(array0)

#arrays in numpy - different
array1 = np.array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])

#arange function shortcut
array2 = np.arange(0, 10, 2)

#zeros function shortcut 
array3 = np.zeros(10)

print(array1)
print(array3)

for i in range(len(array2)):
	print(array2[i])


#multidimensional arrays
multidimensionalArray = np.full((2, 10), 5)
multidimensionalArray = np.array([[1, 2, 3, 4, 5],[6, 7, 8, 9, 10]])
print(multidimensionalArray)
print(multidimensionalArray[0:2, 1:3],"\n")

#iterating through the 2-d array, only printing out the column from 0th column till ith column
for i in range(len(multidimensionalArray[0])):
	print(multidimensionalArray[0:2, i])


#shape of an array
print(multidimensionalArray.shape)

#the number of dimensions (axes) of the array
print(multidimensionalArray.ndim)


#the total number of elements in the array
print(multidimensionalArray.size)
print(array2.size)


#compute the sum of the array using the method .sum()
print(multidimensionalArray.sum())
#print(array2.sum())

#max, min, mean functions 
#print(multidimensionalArray.mean())
#print(multidimensionalArray.max())
#print(multidimensionalArray.min())

#method .reshape() that reshapes an existing array into a shape that is inputted in the parameter of the method
#disclaimer: has to be the same size as the original, if it's 1X10 = size 10
#2X5 = size 10
#print(multidimensionalArray.reshape(1,10))

multidimensionalArray = multidimensionalArray.reshape((5, 2))
#flattens multidimensional arrays
#print(multidimensionalArray.flatten())


#universal function
np1 = np.arange(-3, 10)
print(np1)
number = 23

#square root of each element
#returns an array in this case, the parameter is also an array 
print(np.sqrt(np1))
#works also for normal numbers
#print(np.sqrt(number))

#Absolute value 
#takes arrays, and single-valued numbers and returns the absolute value of the number, or the array of numbers 
print(np.absolute(np1))

#exponentials f(x) = e^x 
#for arrays, and a number
print(np.exp(np1))

#returns -1 for negative numbers, 1 for positive numbers, and 0 for 0
print(np.sign(np1))

#sin cos tan log
#print(np.sin(np1))
#print(np.tan(np1))
#print(np.log(np1))
#print(np.cos(np1))

#more universal functions
#https://numpy.org/doc/stable/reference/ufuncs.html
