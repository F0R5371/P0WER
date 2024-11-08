import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
 
class Graph:
    def __init__(self, x, y):
        self.x = x
        self.y = y

def linear_reg(x, y):
    # Getting mean of x and y values
    x_sum = 0
    for num in x:
        x_sum += num
    x_sum /= len(x)
    
    # Getting mean of y valeus
    y_sum = 0
    for num in y:
        y_sum += num
    y_sum /= len(y)

    # --------------------------

    # Calculating in change in x and y positions
    delta_x = np.empty(len(x))
    for i in range(len(x)):
        delta_x[i] = x[i] - x_sum

    delta_y = np.empty(len(x))
    for i in range(len(y)):
        delta_y[i] = y[i] - y_sum

    # Calculating standard deviation of xy and xx
    std_xy = 0
    std_xx = 0
    for i in range(len(delta_x)):
        std_xy += (delta_x[i] * delta_y[i])
        std_xx += delta_x[i]**2
    
    b = std_xy / std_xx
    a = y_sum - b * x_sum

    # Returns a and b of y = a + bx
    return (a, b)

def evalulate_lin_reg(a, b, arr_x):
    points = [ ]
    # Line is still not straight hmmm...
    for i in range(0, len(arr_x)):
        value = (max(arr_x) / len(arr_x) * i)
        points.append((value * b) + a)
        
    return points

x_val = 0
y_val = 0

x_vals = np.array([5, 7, 12, 16, 20, 25])
y_vals = np.array([40, 120, 180, 210, 240, 270])

eq = linear_reg(x_vals, y_vals)
reg_y = np.array(evalulate_lin_reg(eq[0], eq[1], x_vals))

plt.plot(x_vals, y_vals, 'Hb', ms = 8)
plt.plot(x_vals, reg_y, 'h-g', ms = 8)
plt.show()
