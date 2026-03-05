import pandas as pd
filename = 'tips.csv'
df = pd.read_csv(filename)

dfTip = df.tip

mask = dfTip > 3

#mask to select dinner and lunch rows
maskDinner = df.time == 'Dinner'
maskLunch = df.time == 'Lunch'

#create 2 dataframes
dfDinner = df[maskDinner]
dfLunch = df[maskLunch]

#print(dfDinner.describe())
#print(dfLunch.describe())
#print(df.total_bill.describe())

satOrSun = (df.day == "Sat") | (df.day == "Sun")
df2 = df[maskDinner & satOrSun]
#print(df2.describe())

newMask = (df["tip"] > 3) & (df["time"] == "Lunch")

