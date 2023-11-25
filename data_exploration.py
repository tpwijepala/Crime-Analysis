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
plt.title("Crime Types in January")
df_jan["TYPE"].value_counts().plot(kind="bar")
plt.xlabel("Crime Type")
plt.ylabel("# of Crimes")

plt.subplot(3, 4, 2)
plt.title("Crime Types in February")
plt.xlabel("Crime Type")
plt.ylabel("# of Crimes")
df_feb["TYPE"].value_counts().plot(kind="bar")

plt.subplot(3, 4, 3)
plt.title("Crime Types in March")
plt.xlabel("Crime Type")
plt.ylabel("# of Crimes")
df_mar["TYPE"].value_counts().plot(kind="bar")

plt.subplot(3, 4, 4)
plt.title("Crime Types in April")
plt.xlabel("Crime Type")
plt.ylabel("# of Crimes")
df_apr["TYPE"].value_counts().plot(kind="bar")

plt.subplot(3, 4, 5)
plt.title("Crime Types in May")
plt.xlabel("Crime Type")
plt.ylabel("# of Crimes")
df_may["TYPE"].value_counts().plot(kind="bar")

plt.subplot(3, 4, 6)
plt.title("Crime Types in June")
plt.xlabel("Crime Type")
plt.ylabel("# of Crimes")
df_jun["TYPE"].value_counts().plot(kind="bar")

plt.subplot(3, 4, 7)
plt.title("Crime Types in July")
plt.xlabel("Crime Type")
plt.ylabel("# of Crimes")
df_jul["TYPE"].value_counts().plot(kind="bar")

plt.subplot(3, 4, 8)
plt.title("Crime Types in August")
plt.xlabel("Crime Type")
plt.ylabel("# of Crimes")
df_aug["TYPE"].value_counts().plot(kind="bar")

plt.subplot(3, 4, 9)
plt.title("Crime Types in September")
plt.xlabel("Crime Type")
plt.ylabel("# of Crimes")
df_sep["TYPE"].value_counts().plot(kind="bar")

plt.subplot(3, 4, 10)
plt.title("Crime Types in October")
plt.xlabel("Crime Type")
plt.ylabel("# of Crimes")
df_oct["TYPE"].value_counts().plot(kind="bar")

plt.subplot(3, 4, 11)
plt.title("Crime Types in November")
plt.xlabel("Crime Type")
plt.ylabel("# of Crimes")
df_nov["TYPE"].value_counts().plot(kind="bar")

plt.subplot(3, 4, 12)
plt.title("Crime Types in December")
plt.xlabel("Crime Type")
plt.ylabel("# of Crimes")
df_dec["TYPE"].value_counts().plot(kind="bar")

fig.tight_layout()
plt.show()


