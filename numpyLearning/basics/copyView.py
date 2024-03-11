import numpy as np

#copying vs viewing
np1 = np.array([0, 1, 2, 3, 4, 5])

'''
#create a view
np2 = np1.view()

print(f'Original NP1 {np1}')
print(f'Original NP2 {np2}')

np1[0] = 23

#since np2 is not a copy but a view, if the np1 changes, np2 also changes with np1, view gets changed 
print(f'Changed NP1 {np1}')
print(f'Original NP2 {np2}')
'''

#create a copy
np2 = np1.copy()
print(f'Original NP1 {np1}')
print(f'Original NP2 {np2}')

np1[0] = 23

#creates a copy, doesn't modify the np2 if np1 changes, that's the difference between view and copy
print(f'Changed NP1 {np1}')
print(f'Original NP2 {np2}')


'''
Array Manipulation:

numpy.transpose(): Permute the dimensions of an array.
numpy.concatenate(): Join arrays along an existing axis.
numpy.stack(): Join arrays along a new axis.
numpy.reshape(): Reshape an array.


Mathematical Operations:

numpy.sin(), numpy.cos(), numpy.tan(): Trigonometric functions.
numpy.sqrt(): Square root function.
numpy.abs(): Absolute value function.
numpy.log(), numpy.log10(), numpy.log2(): Logarithmic functions.


Array Statistics:

numpy.mean(): Compute the mean of array elements.
numpy.median(): Compute the median of array elements.
numpy.std(): Compute the standard deviation of array elements.
numpy.var(): Compute the variance of array elements.


Array Searching and Sorting:

numpy.argmax(), numpy.argmin(): Return the indices of the maximum and minimum elements, respectively.
numpy.sort(): Sort elements of an array along a specified axis.
numpy.searchsorted(): Find the indices where elements should be inserted to maintain order.


Random Number Generation:

numpy.random.rand(), numpy.random.randn(): Generate random samples from uniform and normal distributions, respectively.
numpy.random.randint(): Generate random integers from a low (inclusive) to high (exclusive) range.
numpy.random.shuffle(): Modify a sequence in-place by shuffling its contents.


Linear Algebra:

numpy.dot(): Dot product of two arrays.
numpy.linalg.inv(): Compute the inverse of a matrix.
numpy.linalg.det(): Compute the determinant of a matrix.
numpy.linalg.eig(): Compute the eigenvalues and eigenvectors of a square matrix.


Array Comparison and Boolean Operations:

numpy.equal(), numpy.not_equal(), numpy.greater(), numpy.less(), numpy.logical_and(), numpy.logical_or(): Element-wise comparison and boolean operations.


Data Input/Output:

numpy.loadtxt(), numpy.genfromtxt(): Load data from a text file into an array.
numpy.savetxt(): Save an array to a text file.
'''


#iterating through numpy arrays
#1-d
np1 = np.arange(1, 11)

'''
for x in np1:
	print(x)
'''

#2-d
np2 = np.array([np.arange(1, 6), np.arange(5, 11)])
'''
for x in np2:
	for y in x:
		print(y)
'''

#for nth dimension, the runtime becomes very long, a lot of nested for loops
#not so efficient, there's better solutions 

#using np.nditer()
#no loop embedding
#3-d
np3 = np.array([[[1, 2, 3], [4, 5, 6]], [[7, 8, 9], [10, 11, 12]]])
for x in np.nditer(np3):
	print(x)
