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

def sleep_stats(df, col, mask=None):
    if mask is not None:
        df = df.loc[mask]
    s = df[col].dropna()
    w = df.loc[s.index, 'weight']
    total = w.sum()
    insuf = w[s <= 4].sum() / total * 100
    vshort = w[s <= 2].sum() / total * 100
    n = len(s)
    return insuf, vshort, n


# Grade breakdown (q3: 1=9th/Freshman, 2=10th/Sophomore, 3=11th/Junior, 4=12th/Senior)
GRADES = {1: 'Freshman', 2: 'Sophomore', 3: 'Junior', 4: 'Senior'}

print(f"\n{'Grade':<12} {'n_2007':>8} {'2007':>8} {'n_2023':>8} {'2023':>8} {'Change':>8}  (insufficient sleep, <=7hr)")
for code, label in GRADES.items():
    i07, _, n07 = sleep_stats(df07, 'q97', mask=df07['q3'] == code)
    i23, _, n23 = sleep_stats(df23, 'q85', mask=df23['q3'] == code)
    print(f"{label:<12} {n07:>8,} {i07:>7.1f}% {n23:>8,} {i23:>7.1f}% {i23-i07:>+7.1f}%")

