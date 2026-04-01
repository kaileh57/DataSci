import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv('lex.csv')

countries = ['irl', 'usa', 'ind', 'mex']
country_names = {
    'irl': 'Ireland',
    'usa': 'USA',
    'ind': 'India',
    'mex': 'Mexico'
}

data = df[df['geo'].isin(countries)].copy()

years = [str(year) for year in range(1800, 2024)]
id_vars = ['geo', 'name']
value_vars = years
melted = data.melt(id_vars=id_vars, value_vars=value_vars, var_name='Year', value_name='LifeExpectancy')

melted['Year'] = pd.to_numeric(melted['Year'])

plt.figure(figsize=(12, 7))

for country_code in countries:
    country_data = melted[melted['geo'] == country_code]
    plt.plot(country_data['Year'], country_data['LifeExpectancy'], 
             marker='o', linewidth=2, markersize=4, 
             label=country_names[country_code], alpha=0.8)

plt.xlabel('Year', fontsize=12, fontweight='bold')
plt.ylabel('Life Expectancy (years)', fontsize=12, fontweight='bold')
plt.title('Life Expectancy Comparison: Ireland, USA, India, and Mexico (1800-2023)', 
          fontsize=14, fontweight='bold', pad=20)
plt.legend(fontsize=11, loc='best')
plt.grid(True, alpha=0.3)
plt.tight_layout()
plt.savefig('life_expectancy_comparison.png', dpi=300, bbox_inches='tight')
plt.show()

print("Chart saved as 'life_expectancy_comparison.png'")
