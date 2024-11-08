import pandas as pd
import matplotlib as mpl

class Graph:
    def __init__(self, x, y):
        self.x = x
        self.y = y

x_val = 0
y_val = 0

df = pd.DataFrame(
    {
        'Name': ['Joe', 'John', 'Aiden'],
        'Age': [199, 2, 0],
        'Sex': ['Male', 'Dog', 'Male'],
    }
)

print(df)

print()

ser = pd.Series([20, 21, 24], name = 'Years')

print(ser)

print(df['Age'].max())
print(df['Age'].min())

print(df.describe())