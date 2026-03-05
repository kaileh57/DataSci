import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv('tips.csv')

print(df.describe())

print(df.tip.describe())
myColums = ["total_bill", "tip"]
print(df[myColums].describe())
print(df.total_bill.mean())

sns.histplot(data=df, x="tip", bins=20).set(title="Distribution of Tips")
plt.show()

df["tip_percentage"] = df["tip"] / df["total_bill"] * 100
sns.histplot(data=df, x="tip_percentage", bins=20).set(title="Distribution of Tip Percentage")
plt.show()

sns.boxplot(x=df["tip"], y=df["smoker"])
plt.show()

g = sns.FacetGrid(df, col="time")
g = g.map(sns.histplot, "tip")
plt.show()