import pandas as pd
fileName = "penguins.csv"
df = pd.read_csv(fileName)
print(df.body_mass_g.max())
