import matplotlib.pyplot as plt
import numpy as np
# print "3.0"
print(np.sqrt(9))

vec = np.array([3, 4, 5])

# Prints "array([3, 4, 5])"
print(vec)
print(vec.shape)

row_vec = np.array([7, 2, 9])
print(row_vec)

print(row_vec.reshape(1, 3))

col_vec = np.array([3, 1, 7, 4])
print(col_vec.reshape(4, 1))
print(col_vec.reshape(-1, 1))

mat = np.array([[2, 0], [5, 1], [7, -3]])
print(mat)
print(mat.shape)

matrix = np.arange(100).reshape(10, 10)
print(matrix)

arr = np.arange(12)

B = np.array([[5, 0, 3], [2, 8, 4]])
A = np.array([[2, 8], [9, 0], [9, 5]])

A = np.array([0.4, 1.7, 1.2])
A
B = np.array([0.8, 0.9, 0.6])
B
x = np.array([4, 3, 2])
x*5.3
S = np.array([[2, 8], [3, 1]])
S
T = np.array([[0, 1], [1, 1]])
T
ST = S@T
A = np.array([[3, -4], [1, 2], [-3, -1]])
B = np.array([[1, 1], [0, 1], [1, 0]])

A = np.array([[-1, 3/2], [1, -1]])
p = np.array([8, -3, 8, 5, -5])
q = np.array([-4, 8, 7, -1, 6])
a = np.array([[3, 1], [0, 2]])
a @ np.array([3**0.5/2, 0.5]).reshape(-1, 1)
a @ np.array([-2**0.5/2, 2**0.5/2]).reshape(-1, 1)
p = np.array([[0.5, 1, -2], [-4, 2, 1.5]])
v = np.array([3, 4, 1]).reshape(-1, 1)

# np.linspace creates a defined number of evenly spaced data points in a given interval
# In this case, we are creating 10,000 evenly spaced data points between -10, and 10
x_vals = np.linspace(-10, 10, 10_000)

#  Initialize an empty plot
plt.figure()
plt.plot(x_vals, np.sin(x_vals))
plt.plot(x_vals, np.cos(x_vals))
plt.show()
# The code below can go anywhere after plt.figure() and before plt.show()
plt.title("Graph of Sine and Cosine")
plt.plot(x_vals, np.sin(x_vals), label="Sin")
plt.plot(x_vals, np.cos(x_vals), label="Cos")
plt.legend()
plt.xlabel("Input Value")
plt.ylabel("Result Value")
