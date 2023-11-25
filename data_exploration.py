import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.dates import MonthLocator, DateFormatter

# loading cleaned data
cleaned_data = "data/cleaned-data/2022_crimedata.csv"

df = pd.read_csv(cleaned_data)

# Monthly DataFrames 
df_jan = df[df["MONTH"] == 1]
df_feb = df[df["MONTH"] == 2]
df_mar = df[df["MONTH"] == 3]
df_apr = df[df["MONTH"] == 4]
df_may = df[df["MONTH"] == 5]
df_jun = df[df["MONTH"] == 6]
df_jul = df[df["MONTH"] == 7]
df_aug = df[df["MONTH"] == 8]
df_sep = df[df["MONTH"] == 9]
df_oct = df[df["MONTH"] == 10]
df_nov = df[df["MONTH"] == 11]
df_dec = df[df["MONTH"] == 12]

# df["DATE"] = pd.to_datetime(
#     df["YEAR"].astype(str) + df["MONTH"].astype(str), format="%Y%m"
# )

# # Visualizing the distribution of crime types
# plt.figure(figsize=(12, 6))
# df["TYPE"].value_counts().plot(kind="bar", color="skyblue")
# plt.title("Distribution of Crime Types")
# plt.xlabel("Crime Type")
# plt.ylabel("Number of Crimes")
# plt.xticks(rotation=45, ha="right", rotation_mode="anchor")
# plt.show()

# Exploring monthly trends in crimes
monthly_crime = df.groupby("MONTH").size()
plt.figure(figsize=(12, 6))
monthly_crime.plot(marker="o", linestyle="-", color="skyblue")
plt.title("Monthly Crime Trends")
plt.xlabel("Date")
plt.ylabel("Number of Crimes")
plt.show()

# Visualizing distribution of crime types per month
fig = plt.figure(figsize=(12,8))
plt.subplot(3, 4, 1)
df_jan["TYPE"].value_counts().plot(kind="bar")
plt.subplot(3, 4, 2)
df_feb["TYPE"].value_counts().plot(kind="bar")
plt.subplot(3, 4, 3)
df_mar["TYPE"].value_counts().plot(kind="bar")
plt.subplot(3, 4, 4)
df_apr["TYPE"].value_counts().plot(kind="bar")
plt.subplot(3, 4, 5)
df_may["TYPE"].value_counts().plot(kind="bar")
plt.subplot(3, 4, 6)
df_jun["TYPE"].value_counts().plot(kind="bar")
plt.subplot(3, 4, 7)
df_jul["TYPE"].value_counts().plot(kind="bar")
plt.subplot(3, 4, 8)
df_aug["TYPE"].value_counts().plot(kind="bar")
plt.subplot(3, 4, 9)
df_sep["TYPE"].value_counts().plot(kind="bar")
plt.subplot(3, 4, 10)
df_oct["TYPE"].value_counts().plot(kind="bar")
plt.subplot(3, 4, 11)
df_nov["TYPE"].value_counts().plot(kind="bar")
plt.subplot(3, 4, 12)
df_dec["TYPE"].value_counts().plot(kind="bar")

fig.tight_layout()
plt.show()


