import pandas as pd
import numpy as np

filename = 'penguins.csv'
df = pd.read_csv(filename)

maskTorgersen = df.island == 'Torgersen'
maskDream = df.island == 'Dream'
maskAdeline = df.species == 'Adelie'
dfTorgersen = df[maskTorgersen & maskAdeline]
dfDream = df[maskDream & maskAdeline]


import matplotlib.pyplot as plt

#create boxplot of body_mass_g drop NaN values
fig, ax = plt.subplots()
ax.boxplot([dfTorgersen.body_mass_g.dropna(), dfDream.body_mass_g.dropna()], tick_labels=['Torgersen', 'Dream'])
ax.set_title('Body Mass of Adelie Penguins')
ax.set_ylabel('Body Mass (g)')
plt.show()


#expore ratio between bill_length_mm and bill_depth_mm by species and sex
maskMale = df.sex == 'MALE'
maskFemale = df.sex == 'FEMALE'
dfMale = df[maskMale]
dfFemale = df[maskFemale]
fig, ax = plt.subplots()
ax.scatter(dfMale.bill_length_mm, dfMale.bill_depth_mm, label='Male')
ax.scatter(dfFemale.bill_length_mm, dfFemale.bill_depth_mm, label='Female')
ax.set_xlabel('Bill Length (mm)')
ax.set_ylabel('Bill Depth (mm)')
ax.legend()
plt.show()

#visualize which island has the best body mass by species
fig, ax = plt.subplots()
ax.boxplot([df[df.island == 'Torgersen'].body_mass_g.dropna(), df[df.island == 'Dream'].body_mass_g.dropna(), df[df.island == 'Biscoe'].body_mass_g.dropna()], tick_labels=['Torgersen', 'Dream', 'Biscoe'])
ax.set_title('Body Mass of Penguins by Island')
ax.set_ylabel('Body Mass (g)')
plt.show()

#visualize body bass by species
fig, ax = plt.subplots()
ax.boxplot([df[df.species == 'Adelie'].body_mass_g.dropna(), df[df.species == 'Chinstrap'].body_mass_g.dropna(), df[df.species == 'Gentoo'].body_mass_g.dropna()], tick_labels=['Adelie', 'Chinstrap', 'Gentoo'])
ax.set_title('Body Mass of Penguins by Species')
ax.set_ylabel('Body Mass (g)')
plt.show()

#find the median bill ratio
df['bill_ratio'] = df.bill_length_mm / df.bill_depth_mm
median_bill_ratio = df.bill_ratio.median()
print(f'Median Bill Ratio: {median_bill_ratio}')
