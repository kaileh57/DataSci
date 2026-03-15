import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd 

df = pd.read_csv('penguins.csv')

#create a scatterplot between variables of intrest, use color and size and shape to show 4 different variables on one chart 
sns.scatterplot(data=df, x='bill_length_mm', y='bill_depth_mm', hue='species', size='flipper_length_mm', style='sex', palette='Set2', sizes=(20, 200), alpha=0.7)
plt.title('Bill Length vs Bill Depth (size = Flipper Length, color = Species, shape = Sex)')
plt.xlabel('Bill Length (mm)')
plt.ylabel('Bill Depth (mm)')
plt.legend(title='Legend')
plt.show()