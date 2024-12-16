import numpy as np
import pandas as pd



# Task 1

zeros = np.zeros([4,3])
print(zeros)
ones = np.ones([4,3])
print(ones)
shape = np.arange(0,12)
shape = shape.reshape(4,3)
print(shape)

func1 = np.arange(1, 101)
result1 = 2 * func1 ** 2 + 5
print(result1)

func2 = np.arange(-10, 11)
result2 = np.exp(func2*(-1))
print(result2)

# Task 2

euro = pd.read_csv(
    "https://raw.githubusercontent.com/guipsamora/pandas_exercises/master/02_Filtering_%26_Sorting/Euro12/Euro_2012_stats_TEAM.csv"
                   )

df = pd.DataFrame(euro)

print(df[["Team", "Yellow Cards", "Red Cards"]])

print(f' The total number of teams is {df["Team"].count()}')

print(df[df.Goals > 6])

