import pandas as pd

df = pd.read_csv("titanic.csv")

survival_status = {0: "Died", 1: "Survived"}
df["xSurvived"] = df.Survived.replace(survival_status)

c_table = pd.crosstab(index = df["xSurvived"], columns = df["Pclass"], margins = True)
print(c_table)

#use masks to find out if women were more likely to survive
women = df[df.Sex == "female"]
men = df[df.Sex == "male"]
women_survival_rate = women.Survived.mean()
men_survival_rate = men.Survived.mean()
print("Women survival rate:", women_survival_rate)
print("Men survival rate:", men_survival_rate)

#were people with children or spouses more likely to survive?
df["has_family"] = (df["Siblings/Spouses Aboard"] + df["Parents/Children Aboard"]) > 0
family_survival_rate = df[df.has_family].Survived.mean()
no_family_survival_rate = df[~df.has_family].Survived.mean()
print(df[["has_family", "Survived"]].groupby("has_family").mean())

#some visualizations
import matplotlib.pyplot as plt
import seaborn as sns
sns.set_theme()
sns.countplot(data = df, x = "xSurvived", hue = "Sex", palette = ["lightblue", "salmon"])
plt.show()
