import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv('internet_users.csv')

countries = ['irl', 'usa', 'ind', 'chn']
country_names = {
    'irl': 'Ireland',
    'usa': 'USA',
    'ind': 'India',
    'chn': 'China'
}

data = df[df['geo'].isin(countries)].copy()

years = [str(year) for year in range(1995, 2025)]
id_vars = ['geo', 'name']
value_vars = [year for year in years if year in data.columns]

melted = data.melt(id_vars=id_vars, value_vars=value_vars, var_name='Year', value_name='InternetUsers')

melted['Year'] = pd.to_numeric(melted['Year'])
melted['InternetUsers'] = pd.to_numeric(melted['InternetUsers'], errors='coerce')
melted = melted.dropna()

plt.figure(figsize=(12, 7))

for country_code in countries:
    country_data = melted[melted['geo'] == country_code]
    plt.plot(country_data['Year'], country_data['InternetUsers'], marker='o', linewidth=2, markersize=5, label=country_names[country_code], alpha=0.8)

plt.xlabel('Year', fontsize=12, fontweight='bold')
plt.ylabel('Internet Users (% of population)', fontsize=12, fontweight='bold')
plt.title('Internet Users Comparison: Ireland, USA, India, and China (1995-2024)', fontsize=14, fontweight='bold', pad=20)
plt.legend(fontsize=11, loc='best')
plt.grid(True, alpha=0.3)
plt.ylim(0, 105)
plt.tight_layout()
plt.savefig('internet_users_comparison.png', dpi=300, bbox_inches='tight')
plt.show()

print("Chart saved as 'internet_users_comparison.png'")
