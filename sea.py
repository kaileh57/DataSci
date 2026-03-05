import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("tips.csv")

sizes = df["day"].value_counts()
sizes.plot.pie()
plt.show()


sns.set_theme()

day_order = ["Thur", "Fri", "Sat", "Sun"]
sns.countplot(data = df, x = "day", order = day_order)
sns.countplot(data = df, x = "day", hue = "time", palette = ["lightblue", "salmon"], order = day_order)
plt.show()