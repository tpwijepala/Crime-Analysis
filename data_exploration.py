import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.dates import MonthLocator, DateFormatter

# loading cleaned data
cleaned_data = "data/cleaned-data/2022_crimedata.csv"

df = pd.read_csv(cleaned_data)

df["DATE"] = pd.to_datetime(
    df["YEAR"].astype(str) + df["MONTH"].astype(str), format="%Y%m"
)

# Visualizing the distribution of crime types
plt.figure(figsize=(12, 6))
df["TYPE"].value_counts().plot(kind="bar", color="skyblue")
plt.title("Distribution of Crime Types")
plt.xlabel("Crime Type")
plt.ylabel("Number of Crimes")
plt.xticks(rotation=45, ha="right", rotation_mode="anchor")
plt.show()

# Exploring monthly trends in crimes
monthly_crime = df.groupby("DATE").size()
plt.figure(figsize=(12, 6))
monthly_crime.plot(marker="o", linestyle="-", color="skyblue")
plt.title("Monthly Crime Trends")
plt.xlabel("Date")
plt.ylabel("Number of Crimes")
plt.show()
