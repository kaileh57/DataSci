import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

df07 = pd.read_csv('2007_YRBS_data.csv', low_memory=False)
df23 = pd.read_csv('2023_YRBS_data.csv', low_memory=False)

# Sleep question: 1=<=4hr, 2=5hr, 3=6hr, 4=7hr, 5=8hr, 6=9hr, 7=>=10hr
# 2007: q97, 2023: q85
# Insufficient sleep = <8hr = codes 1-4
# Very short sleep = <=5hr = codes 1-2

def sleep_stats(df, col):
    s = df[col].dropna()
    w = df.loc[s.index, 'weight']
    total = w.sum()
    insuf = w[s <= 4].sum() / total * 100
    vshort = w[s <= 2].sum() / total * 100
    return insuf, vshort

insuf07, vshort07 = sleep_stats(df07, 'q97')
insuf23, vshort23 = sleep_stats(df23, 'q85')

print(f"Insufficient sleep (<8hr): 2007={insuf07:.1f}%, 2023={insuf23:.1f}%, change={insuf23-insuf07:+.1f}%")
print(f"Very short sleep (<=5hr):  2007={vshort07:.1f}%, 2023={vshort23:.1f}%, change={vshort23-vshort07:+.1f}%")
