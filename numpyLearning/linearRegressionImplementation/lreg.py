'''
Implementing Linear Regression: 

Implement a simple linear regression model using NumPy. This involves creating synthetic data, 
defining a cost function (e.g., mean squared error), and using gradient descent to optimize the 
model parameters.
'''
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

np.random.seed(0)

'''
Linear Regression is a fundamental statistical method used for modeling the relationship between 
a dependent variable and one or more indpendent variables. In simple linear regression, there is only
one independent variable. It's commonly used for prediction and forecasting. For example,

it can be used to predict sales based on advertising expenditure, predict house prices based on features like
square footage and number of bedrooms, etc.
'''


'''
Creating a simple linear regression model using NumPy:

Define the model: 
In simple linear regression, the relationship between the independent variable X and dependent variable
y is modeled as y=mx+b, where m is the slope and b is the y-intercept.

Generate synthetic data:
Create synthetic data points that follow a linear relationship. This involves randomly generating values for
X and calculating the corresponding values for y, possibly adding some noise to simulate real-world scenarios.

Define the cost function:
Typically, mean squared error (MSE) is used as the cost function for linear regression. It measures the average
squared difference between the actual and predicted values.

Optimize parameters using gradient descent: 
Gradient descent is an optimization algorithm used to minimize the cost function. It iteratively updates the 
parameters (slope and intercept in this case) in the direction of the steepest descent of the cost function
until convergence.
'''


'''
Step-by-step tasks:

1. Generate synthetic data: Create synthetic data points
X and corresponding y values.
2. Initialize parameters: Initialize the slope m and intercept b with random values.
3. Define the cost function: Implement mean squared error (MSE) as the cost function.
4. Implement gradient descent: Update parameters using the gradient descent algorithm to minimize the cost function.
5. Iterate until convergence: Repeat the gradient descent steps until the change in cost function becomes negligible.
'''
#helper function: mean_squared_error
def mean_squared_error(y_true, y_pred):
	return np.mean((y_true - y_pred) ** 2)


#creating synethtic noise
num_samples = 100
x = np.random.rand(num_samples, 1)
epsilon = np.random.randn(num_samples, 1)
y = 2 * x + epsilon
print(x)


#initialize parameters
#slope and y-intercept with random values
m = np.random.randn()
b = np.random.randn()

#define the cost function: (mean squared error)
learning_rate = 0.01
num_iterations = 1000
cost_history = []

for i in range(num_iterations):
	#calculate predictions
	y_pred = m*x + b
	#calculate gradients
	d_m = (-2/num_samples) * np.sum(x * (y - y_pred)) 
	d_b = (-2/num_samples) * np.sum(y-y_pred)

	#update parameters using gradients
	m -= learning_rate * d_m 
	b -= learning_rate * d_b

	#calculate and record cost
	cost = mean_squared_error(y, y_pred) 
	cost_history.append(cost) 
	
	#print progress
	if i % 100 == 0:
		print(f"Iteration {i}: Cost = {cost}")


#finally, plotting the data and linear regression line
plt.scatter(x, y, label="Data")
plt.plot(x, m*x+b, color = "red", label = "Regression line")
plt.xlabel("x")
plt.ylabel("y")
plt.title("Simple Linear Regression")
plt.legend()
plt.show()

print("Final parameters:")
print("Slope (m):", m)
print("Intercept (b):", b)
print("Final cost:", cost_history[-1])
