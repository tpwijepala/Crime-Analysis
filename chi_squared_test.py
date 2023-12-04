import os
import pandas as pd
import numpy as np
from scipy import stats

# loading cleaned data
cleaned_files = [file for file in os.listdir("data/cleaned-data/")]

df = pd.DataFrame()
for file in cleaned_files:
    data = pd.read_csv("data/cleaned-data/"+file)
    df = pd.concat([df, data])

df = df.groupby(["YEAR","MONTH", "NEIGHBOURHOOD"]).size().to_frame("SIZE")
df = df.reset_index()

contingency = pd.pivot_table(
    df[["MONTH","SIZE","NEIGHBOURHOOD"]],
    values="SIZE",
    index="MONTH",
    columns="NEIGHBOURHOOD",
    fill_value=0
    )

print(contingency)
chi2, p, dof, expected = stats.chi2_contingency(contingency)
print(p)
# print(expected)