import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
 
class Graph:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def graph(self, color):
        plt.plot(self.x, self.y, f'H{color}')
        plt.show()

class LinearGraph(Graph):
    def evaluate_lin_reg(self, a, b, val):
        # Line is still not straight hmmm...
        new_val = (val * b) + a
        return new_val

    def linear_reg_eq(self, x, y):
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

    def graph(self, color, color2):
        eq = self.linear_reg_eq(self.x, self.y)

        x_reg = np.array([min(self.x), max(self.x)])
        y_reg = np.array([self.evaluate_lin_reg(eq[0], eq[1], x_reg[0]), self.evaluate_lin_reg(eq[0], eq[1], x_reg[1])])

        plt.plot(self.x, self.y, f'H{color}')
        plt.plot(x_reg, y_reg, f'h-{color2}', ms = 0)
        plt.show()

x_vals = []
y_vals = []

#lin_grp = LinearGraph(x_vals, y_vals)
#lin_grp.graph('b', 'g')