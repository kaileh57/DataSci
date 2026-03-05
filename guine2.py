import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv('penguins.csv')

print(df.describe())

# sns.boxplot(x='species', y='body_mass_g', data=df)
# plt.title('Boxplot of Body Mass by Penguin Species')
# plt.xlabel('Penguin Species')
# plt.ylabel('Body Mass (g)')
# plt.show()

sns.histplot(data=df, x='body_mass_g', hue='species', kde=True)
plt.title('Distribution of Body Mass by Penguin Species')
plt.xlabel('Body Mass (g)')
plt.ylabel('Frequency')
plt.show()

# sns.histplot(data=df, x='bill_length_mm', hue='species', kde=True)
# plt.title('Distribution of Bill Length by Penguin Species')
# plt.xlabel('Bill Length (mm)')
# plt.ylabel('Frequency')
# plt.show()

# use facetgrid to create histograms of body mass by island and species
g = sns.FacetGrid(df, col='island', row='species', margin_titles=True)
g.map(sns.histplot, 'body_mass_g', kde=True)
g.set_axis_labels('Body Mass (g)', 'Frequency')
g.figure.suptitle('Distribution of Body Mass by Island and Penguin Species', y=1.02)
plt.show()