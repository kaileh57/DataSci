import pandas as pd
import plotly.express as px


fileName1 = "gdp_pcap.csv"
df_GDP = pd.read_csv(fileName1)

fileName2 = "internet_users.csv"
df_internet = pd.read_csv(fileName2)    # internet users %

fileNameCountries = "country_info.csv"
df_countries = pd.read_csv(fileNameCountries)

year = "2023"

myColumns = ["geo", "name", year]

df1 = df_GDP[myColumns].rename(columns = {year: "GDP"}) 

df2 = df_internet[myColumns].rename(columns = {year: "internet_users"})

# merge the two dataframes

df = pd.merge(df1, df2, on = "geo")
df = pd.merge(df, df_countries[["geo", "four_regions"]], on = "geo")

# now make a scatterplot with plotly
plt = px.scatter(data_frame = df, x = "GDP", y = "internet_users",
                 color = "four_regions", size_max = 10, opacity = 0.8,
                 hover_data = ["name_x"],
                 title = year + " internet users vs. GDP",
                 labels = {"GDP": "GDP per capita (2023 international dollars)",
                          "internet_users": "Internet users (%)"})

plt.update_xaxes(type = "log")

plt.show()