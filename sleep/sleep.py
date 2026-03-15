import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

df = pd.read_csv('2023_YRBS_data.csv', low_memory=False)

myColumns = ["q1", "q2", "q3"]
dfsmall = df[myColumns]

names = {"q1":"age", "q2":"sex", "q3":"grade"}
dfsmall = dfsmall.rename(columns=names)

gradeCodes = {1:"9th Grade", 2:"10th Grade", 3:"11th Grade", 4:"12th Grade", 5:"Other"}
dfsmall["gradeX"] =dfsmall.grade.replace(gradeCodes)
dfsmall["gradeX"] = dfsmall.gradeX.fillna("Missing")

sexCodes = {1:"Male", 2:"Female"}
dfsmall["sexX"] = dfsmall.sex.replace(sexCodes)
dfsmall["sexX"] = dfsmall.sexX.fillna("Missing")


print(dfsmall.gradeX.value_counts())
print(dfsmall.sexX.value_counts())

