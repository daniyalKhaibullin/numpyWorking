'''
Matrix Operations:

Write functions to perform basic matrix 
operations such as addition, subtraction, 
multiplication, and transposition using NumPy arrays.
Implement functions for matrix inversion and determinant
calculation using NumPy's linear algebra functions (numpy.linalg.inv(), numpy.linalg.det()).
'''
import numpy as np


class matrixManipulation:
	matrix = []


	def __init__(self, matrix):
		self.matrix = matrix 
	
	def addition(self, matrix2):
		'''
		Perform matrix addition.

    Parameters:
				self (numpy.ndarray): First matrix.
        matrix2 (numpy.ndarray): Second matrix.

    Returns:
        numpy.ndarray: Result of the addition.
		'''
		#or return np.add(self.matrix + matrix2)
		return self.matrix + matrix2
		

	def subtraction(self, matrix2):
		'''
    Perform matrix subtraction.

    Parameters:
        self (numpy.ndarray): First matrix.
        matrix2 (numpy.ndarray): Second matrix.

    Returns:
        numpy.ndarray: Result of the subtraction.
   	''' 
		return np.subtract(self.matrix, matrix2)

	
	def multiplication(self, matrix2):
		'''	
    Perform matrix multiplication.

    Parameters:
        self (numpy.ndarray): First matrix.
        matrix2 (numpy.ndarray): Second matrix.

    Returns:
        numpy.ndarray: Result of the multiplication.
   	''' 
		return np.matmul(self.matrix, matrix2)
	
	def transposition(self):
		"""
    Perform matrix transposition.

    Parameters:
        self (numpy.ndarray): instance variable matrix.

    Returns:
        numpy.ndarray: Transposed matrix.
    """
		return np.transpose(self.matrix)


	def matrix_inversion(self):
		'''
    Calculate the inverse of a matrix.

    Parameters:
        self (numpy.ndarray): Instance variable matrix.

    Returns:
        numpy.ndarray: Inverse of the matrix.
				using numpy.linalg - for linear algebra operations
   	''' 
		return np.linalg.inv(self.matrix)


	def matrix_determinant(self):
		'''
    Calculate the determinant of a matrix.

    Parameters:
        self (numpy.ndarray): Instance variable matrix.

    Returns:
        float: Determinant of the matrix.
		'''
		return np.linalg.det(self.matrix)


def main():
	#creating an object of matrix
	matrix = matrixManipulation(np.array([[1, 2, 3], [4, 5, 6]]))

	#creating a second matrix
	np2 = np.array([np.arange(1, 4), np.arange(4, 7)])

	#addition
	print(matrix.addition(np2))

	#subtraction

if __name__ == "__main__":
	main()

#marked by ChatGPT as 5/5