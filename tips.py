import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

fileName = "tips.csv"
df = pd.read_csv(fileName)

day_sizes = df.day.value_counts()
print(day_sizes)

N = len(df)
rel_day_sizes = df.day.value_counts() / N * 100
print(rel_day_sizes)

c_table = pd.crosstab(index = df["day"], columns = df["time"], margins = True)
perc_table = pd.crosstab(index = df["day"], columns = df["time"], margins = True, normalize = True)

print(c_table)
print(perc_table)
