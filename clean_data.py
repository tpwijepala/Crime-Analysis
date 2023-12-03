import sys
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import OneHotEncoder
from sklearn.linear_model import LinearRegression
from sklearn.compose import ColumnTransformer
from sklearn.ensemble import RandomForestRegressor
import utm

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

approx_utm_coords = {
    "Central Business District": {"X": 491493.3146, "Y": 5459541.9753},
    "Renfrew-Collingwood": {"X": 495958.4128, "Y": 5454219.578},
    "Hastings-Sunrise": {"X": 495897.2912, "Y": 5458709.6784},
    "Mount Pleasant": {"X": 492644.7214, "Y": 5456749.5725},
    "Victoria-Fraserview": {"X": 494409.0105, "Y": 5453316.1714},
    "West Point Grey": {"X": 486451.1627, "Y": 5457537.8003},
    "Marpole": {"X": 489766.1375, "Y": 5450967.6983},
    "Stanley Park": {"X": 490124.2541, "Y": 5460764.8808},
    "West End": {"X": 490247.4903, "Y": 5459171.3852},
    "Kitsilano": {"X": 489317.4997, "Y": 5457464.529},
    "Fairview": {"X": 489925.4636, "Y": 5456850.491},
    "Strathcona": {"X": 494011.8703, "Y": 5458691.2305},
    "Grandview-Woodland": {"X": 494944.6566, "Y": 5457903.8889},
    "Kensington-Cedar Cottage": {"X": 494241.6543, "Y": 5455425.5902},
    "Oakridge": {"X": 491410.1615, "Y": 5451820.6407},
    "Sunset": {"X": 493883.5176, "Y": 5452404.9326},
    "Riley Park": {"X": 492650.6285, "Y": 5455798.3804},
    "Killarney": {"X": 496784.8536, "Y": 5450446.0664},
    "Musqueam": {"X": 485483.593, "Y": 5452748.6444},
    "Dunbar-Southlands": {"X": 486516.4442, "Y": 5455132.9432},
    "Kerrisdale": {"X": 488716.933, "Y": 5453017.0802},
    "Arbutus Ridge": {"X": 488595.4253, "Y": 5453651.5645},
    "Shaughnessy": {"X": 490649.8186, "Y": 5454311.084},
    "South Cambie": {"X": 491598.5258, "Y": 5455188.0781},
}

for neighbourhood, utm_coords in approx_utm_coords.items():
    df.loc[(df["NEIGHBOURHOOD"] == neighbourhood) | (df["X"] == 0.0), "X"] = utm_coords[
        "X"
    ]
    df.loc[(df["NEIGHBOURHOOD"] == neighbourhood) | (df["Y"] == 0.0), "Y"] = utm_coords[
        "Y"
    ]


# changing UTM -> lat and lon
# https://stackoverflow.com/questions/49890492/convert-utm-to-lat-long-in-csv-using-pandas
def utmToLatlon(row):
    if row["X"] == 0 and row["Y"] == 0:
        return pd.Series({"LAT": "NULL", "LON": "NULL"})

    lat, lon = utm.to_latlon(row["X"], row["Y"], 10, northern=True)
    return pd.Series({"LAT": lat, "LON": lon})


df = df.merge(df.apply(utmToLatlon, axis=1), left_index=True, right_index=True)

df.drop(columns=["X", "Y"], inplace=True)


""" Note that some crimes are similiar:
B&E Commerical & B&E res/other,
Theft From Vehicle, Theft of Bicycle & Theft of Vehicle,
Car Crash (w/ Fatality), Car Crash (w/ Injury)

Will need to take into account the similiarities/Differences when analyzing data"""

df = df[["YEAR", "MONTH", "TYPE", "NEIGHBOURHOOD", "LAT", "LON"]]
df = df.sort_values(by=["YEAR", "MONTH", "TYPE", "NEIGHBOURHOOD", "LAT", "LON"])

df.to_csv(cleaned_data_file, index=False)
