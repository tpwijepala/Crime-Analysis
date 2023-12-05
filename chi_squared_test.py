import os
import pandas as pd
import dataframe_image as dfi
import numpy as np
from scipy import stats

# loading cleaned data
cleaned_files = [file for file in os.listdir("data/cleaned-data/")]

df = pd.DataFrame()
for file in cleaned_files:
    data = pd.read_csv("data/cleaned-data/" + file)
    df = pd.concat([df, data])


df_monthly = df.groupby(["YEAR", "MONTH"]).size().to_frame("Number of Crimes")
df_monthly = df_monthly.reset_index()

monthly_distribtuion = pd.pivot_table(
    df_monthly[["MONTH", "Number of Crimes"]], columns="MONTH", fill_value=0
)

dfi.export(monthly_distribtuion, "chi2-png/monthly-distribution.png")
monthly_distribtuion = monthly_distribtuion.to_numpy()[0]
chi_2, p = stats.chisquare(monthly_distribtuion)
print(p)

df_neighbourhood = (
    df.groupby(["YEAR", "MONTH", "NEIGHBOURHOOD"]).size().to_frame("Number of Crimes")
)
df_neighbourhood = df_neighbourhood.reset_index()

neighbourhood_month_contingency = pd.pivot_table(
    df_neighbourhood[["MONTH", "Number of Crimes", "NEIGHBOURHOOD"]],
    values="Number of Crimes",
    index="MONTH",
    columns="NEIGHBOURHOOD",
    fill_value=0,
)


dfi.export(
    neighbourhood_month_contingency, "chi2-png/neighbourhood-month-contingency.png"
)
neighbourhood_month_contingency = neighbourhood_month_contingency.to_numpy()

chi2, p, dof, expected = stats.chi2_contingency(neighbourhood_month_contingency)
print(p)

df_crime_type = (
    df.groupby(["YEAR", "MONTH", "TYPE"]).size().to_frame("Number of Crimes")
)
df_crime_type = df_crime_type.reset_index()

crime_type_month_contingency = pd.pivot_table(
    df_crime_type[["MONTH", "Number of Crimes", "TYPE"]],
    values="Number of Crimes",
    index="MONTH",
    columns="TYPE",
    fill_value=0,
)


dfi.export(crime_type_month_contingency, "chi2-png/crime-type-month-contingency.png")
crime_type_month_contingency = crime_type_month_contingency.to_numpy()

chi2, p, dof, expected = stats.chi2_contingency(crime_type_month_contingency)
print(p)
