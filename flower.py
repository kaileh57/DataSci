import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

df = pd.read_csv('iris.csv')

df['PetalArea'] = df['PetalLengthCm'] * df['PetalWidthCm']

species_list = df['Species'].unique()
palette = sns.color_palette('deep', len(species_list))
color_map = dict(zip(species_list, palette))

fig, ax = plt.subplots()

sns.scatterplot(
    data=df, x='SepalLengthCm', y='SepalWidthCm',
    hue='Species', size='PetalArea', sizes=(20, 200),
    palette=color_map, alpha=0.7, ax=ax
)

for species in species_list:
    subset = df[df['Species'] == species]
    a, b = np.polyfit(subset['SepalLengthCm'], subset['SepalWidthCm'], 1)
    x_vals = np.linspace(subset['SepalLengthCm'].min(), subset['SepalLengthCm'].max(), 100)
    ax.plot(x_vals, a * x_vals + b, color=color_map[species], linestyle='--', linewidth=2)

ax.set_title('Sepal Length vs Sepal Width (size = Petal Area)')
plt.show()