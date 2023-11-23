import pandas as pd
import matplotlib.pyplot as plt

# loading cleaned data
cleaned_data = "data/cleaned-data/2022_crimedata.csv"

df = pd.read_csv(cleaned_data)

# Visualizing the distribution of crime types
plt.figure(figsize=(12, 6))
df["TYPE"].value_counts().plot(kind="bar", color="skyblue")
plt.title("Distribution of Crime Types")
plt.xlabel("Crime Type")
plt.ylabel("Number of Crimes")
plt.xticks(rotation=45, ha="right", rotation_mode="anchor")
plt.show()
