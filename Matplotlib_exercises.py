import matplotlib.pyplot as plt
import numpy as np

# np.linspace creates a defined number of evenly spaced data points in a given interval
# In this case, we are creating 10,000 evenly spaced data points between -10, and 10
'''
x_vals = np.linspace(-10, 10, 10_000)

#  Initialize an empty plot
plt.figure()
plt.plot(x_vals, np.sin(x_vals))
plt.plot(x_vals, np.cos(x_vals))

# The code below can go anywhere after plt.figure() and before plt.show()
plt.title("Graph of Sine and Cosine")
plt.plot(x_vals, np.sin(x_vals), label="Sin")
plt.plot(x_vals, np.cos(x_vals), label="Cos")
plt.legend()
plt.xlabel("Input Value")
plt.ylabel("Result Value")
# plt.show()
'''

'''
# Scatter plots
plt.figure()
vals = np.random.rand(15)
# plt.plot(vals)
# plt.plot(vals, marker='o')
# plt.show()
plt.plot(vals, color = 'blue' marker = 'o')
plt.title("Plot of Random Data")
plt.xlabel("Point Number")
plt.ylabel("Random Value")
plt.show()
'''
mean = [0, 0]
cov = [[1, 1], [1, 2]]
x, y = np.random.multivariate_normal(mean, cov, 20).T

plt.figure()
plt.scatter(x, y)
plt.show()

tmp = pd.Series([
    ...: 0.71  0.63  0.85  0.44
    ...: 0.61  0.69  0.92  0.55
    ...: 0.72  0.77  0.92  0.60
    ...: 0.83  0.80  1.00  0.77
    ...: 0.92  1.00  1.24  1.00
    ...: 1.16  1.30  1.45  1.25
    ...: 1.26  1.38  1.86  1.56
    ...: 1.53  1.59  1.83  1.86
    ...: 1.53  2.07  2.34  2.25
    ...: 2.16  2.43  2.70  2.25
    ...: 2.79  3.42  3.69  3.60
    ...: 3.60  4.32  4.32  4.05
    ...: 4.86  5.04  5.04  4.41
    ...: 5.58  5.85  6.57  5.31
    ...: 6.03  6.39  6.93  5.85
    ...: 6.93  7.74  7.83  6.12
    ...: 7.74  8.91  8.28  6.84
    ...: 9.54 10.26  9.54  8.73
    ...: 11.88 12.06 12.15  8.91
    ...: 14.04 12.96 14.85  9.99
    ...: 16.20 14.67 16.02 11.61
    ...:], index=[1960:1980.25:.25])
