import sys
import pandas as pd

# input_file = sys.argv[1]
# output_file = sys.argv[1]

# temp file name
input_file = "data/pre-processed-data/crimedata_csv_AllNeighbourhoods_2022.csv"
output_file = "data/cleaned-data/2022_crimedata.csv"

df = pd.read_csv(input_file)

df = df.drop(["DAY", "HOUR", "MINUTE", "HUNDRED_BLOCK", "X", "Y"], axis=1)

# df_categories = df["TYPE"].unique()
# print(df_categories)

rename_mapping = {
    "Break and Enter Commercial": "B&E-C",
    "Break and Enter Residential/Other": "B&E-R/O",
    "Homicide": "Homicide",
    "Mischief": "Mischief",
    "Offence Against a Person": "Assault",
    "Other Theft": "Theft-O",
    "Theft from Vehicle": "Theft-FV",
    "Theft of Bicycle": "Theft-OB",
    "Theft of Vehicle": "Theft-OV",
    "Vehicle Collision or Pedestrian Struck (with Fatality)": "CC-F",
    "Vehicle Collision or Pedestrian Struck (with Injury)": "CF-I",
}
df["TYPE"] = df["TYPE"].map(rename_mapping)


# checking for missing values
missing_values = df.isnull().sum()
print("\nMissing Values:")
print(missing_values)

# Drop rows with missing values
df.dropna(subset=["NEIGHBOURHOOD"], inplace=True)
print(df)


# Checking data types
# print("\nData Types:")
# print(df.dtypes)


df_categories_new = df["TYPE"].unique()
# print(df_categories_new)

""" Note that some crimes are similiar:
B&E Commerical & B&E res/other,
Theft From Vehicle, Theft of Bicycle & Theft of Vehicle,
Car Crash (w/ Fatality), Car Crash (w/ Injury)

Will need to take into account the similiarities/Differences when analyzing data"""

df = df[["YEAR", "MONTH", "TYPE", "NEIGHBOURHOOD"]]
df = df.sort_values(by=["YEAR", "MONTH", "TYPE", "NEIGHBOURHOOD"])

df.to_csv(output_file, index=False)

# print(df)