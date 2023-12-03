import sys
import pandas as pd
import utm

data_year = sys.argv[1]

preprocessed_data_file = f"data/pre-processed-data/crimedata_csv_AllNeighbourhoods_{data_year}.csv"
cleaned_data_file = f"data/cleaned-data/{data_year}_crimedata.csv"


df = pd.read_csv(preprocessed_data_file)

df = df.drop(["DAY", "HOUR", "MINUTE", "HUNDRED_BLOCK"], axis=1)

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

df_categories_new = df["TYPE"].unique()

#changing UTM -> lat and lon
#https://stackoverflow.com/questions/49890492/convert-utm-to-lat-long-in-csv-using-pandas

def utmToLatlon(row):
    if (row["X"]==0 and row["Y"]==0):
         return pd.Series({"LAT": 'NULL', "LON": 'NULL'})
    
    lat, lon = utm.to_latlon(row["X"], row["Y"], 10, northern=True)
    return pd.Series({"LAT": lat, "LON": lon})

df = df.merge(df.apply(utmToLatlon, axis=1), left_index=True, right_index=True)

df.drop(columns=['X', 'Y'], inplace=True)



""" Note that some crimes are similiar:
B&E Commerical & B&E res/other,
Theft From Vehicle, Theft of Bicycle & Theft of Vehicle,
Car Crash (w/ Fatality), Car Crash (w/ Injury)

Will need to take into account the similiarities/Differences when analyzing data"""

df = df[["YEAR", "MONTH", "TYPE", "NEIGHBOURHOOD", "LAT", "LON"]]
df = df.sort_values(by=["YEAR", "MONTH", "TYPE", "NEIGHBOURHOOD", "LAT", "LON"])

df.to_csv(cleaned_data_file, index=False)
