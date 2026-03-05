import pandas as pd
import time
import numpy as np


# fill grades with 20000 numbers
grades = pd.Series(np.random.randint(0, 100, size=1000))

start = time.perf_counter()

total = 0
for grade in grades:
    total += grade
print(total/len(grades))

end = time.perf_counter()

print(f"Execution time: {end - start:.6f} seconds")

start = time.perf_counter()

total = np.sum(grades)
print(total/len(grades))

end = time.perf_counter()
print(f"Execution time: {end - start:.6f} seconds")
