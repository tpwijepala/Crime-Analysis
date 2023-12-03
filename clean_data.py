import sys
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import OneHotEncoder
from sklearn.linear_model import LinearRegression
from sklearn.compose import ColumnTransformer
from sklearn.ensemble import RandomForestRegressor

# input_file = sys.argv[1]
# output_file = sys.argv[2]

# preprocessed_data_file = f"data/pre-processed-data/{input_file}"
# cleaned_data_file = f"data/cleaned-data/{output_file}"


preprocessed_data_file = (
    "data/pre-processed-data/crimedata_csv_AllNeighbourhoods_2022.csv"
)
cleaned_data_file = "data/cleaned-data/2022_crimedata.csv"

df = pd.read_csv(preprocessed_data_file)

df = df.drop(["DAY", "HOUR", "MINUTE"], axis=1)

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

df.dropna(subset=["NEIGHBOURHOOD"], inplace=True)


""" Note that some crimes are similiar:
B&E Commerical & B&E res/other,
Theft From Vehicle, Theft of Bicycle & Theft of Vehicle,
Car Crash (w/ Fatality), Car Crash (w/ Injury)

Will need to take into account the similiarities/Differences when analyzing data"""

df = df[["YEAR", "MONTH", "TYPE", "NEIGHBOURHOOD", "X", "Y"]]
df = df.sort_values(by=["YEAR", "MONTH", "TYPE", "NEIGHBOURHOOD"])

df.to_csv(cleaned_data_file, index=False)
