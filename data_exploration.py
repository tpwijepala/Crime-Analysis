import os
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.dates import MonthLocator, DateFormatter

# loading cleaned data
cleaned_files = [file for file in os.listdir("data/cleaned-data/")]

df = pd.DataFrame()
for file in cleaned_files:
    data = pd.read_csv("data/cleaned-data/"+file)
    df = pd.concat([df, data])

# Monthly DataFrames
num_of_years = df["YEAR"].max() - df["YEAR"].min() + 1
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

months = [
    "jan",
    "feb",
    "mar",
    "apr",
    "may",
    "jun",
    "jul",
    "aug",
    "sep",
    "oct",
    "nov",
    "dec",
]

def crime_rate_trends():
    df["DATE"] = pd.to_datetime(df["YEAR"].astype(str) + df["MONTH"].astype(str), format="%Y%m")
    plt.figure(figsize=(12,8))
    plt.ylabel("# of Crimes")
    plt.xlabel("DATE")
    plt.title("Crime Rate Trends")
    crime_rates = df.groupby("DATE").size()
    crime_rates.plot(marker="o", linestyle="-", color="blue")
    plt.savefig("crime-rate-trends.png")
    

def monthly_crime_rate():
    # Exploring monthly trends in crimes
    monthly_crime = df.groupby(["YEAR","MONTH"]).size()
    monthly_crime = monthly_crime.groupby("MONTH").mean()
    plt.figure(figsize=(12, 8))
    monthly_crime.plot(marker="o", linestyle="-", color="blue")
    plt.title("Monthly Crime Trends")
    plt.xlabel("Month")
    plt.ylabel("Number of Crimes")
    plt.savefig("monthly_trends.png")


def crime_type_trends():
    xlabels = np.arange(1, 13)

    plt.figure(figsize=(9, 6))
    plt.title("Monthly Break & Enter Rates")
    plt.xlabel("Month")
    plt.ylabel("# of Crimes")
    df_BE = (
        df[(df["TYPE"] == "B&E-C") | (df["TYPE"] == "B&E-R/O")].groupby(["YEAR","MONTH"]).size()
    )
    df_BE = df_BE.groupby("MONTH").mean()
    df_BE.plot(marker="o", linestyle="-", color="blue")
    plt.xticks(xlabels, rotation=0)
    plt.savefig("crime-type-trends-png/B&E.png")

    plt.figure(figsize=(9, 6))
    plt.title("Monthly Homicide Rates")
    plt.xlabel("Month")
    plt.ylabel("# of Crimes")
    df_homicide = df[df["TYPE"] == "Homicide"].groupby(["YEAR","MONTH"]).size()
    df_homicide = df_homicide.groupby("MONTH").mean()
    # filling in empty months with 0
    new_index = pd.Index(xlabels, name="MONTH")
    df_homicide = df_homicide.reindex(new_index, fill_value=0)
    df_homicide.plot(marker="o", linestyle="-", color="blue")
    plt.xticks(xlabels, rotation=0)
    plt.savefig("crime-type-trends-png/Homicide.png")

    plt.figure(figsize=(9, 6))
    plt.title("Monthly Mischief Rates")
    plt.xlabel("Month")
    plt.ylabel("# of Crimes")
    df_mischief = df[df["TYPE"] == "Mischief"].groupby(["YEAR","MONTH"]).size()
    df_mischief = df_mischief.groupby("MONTH").mean()
    df_mischief.plot(marker="o", linestyle="-", color="blue")
    plt.xticks(xlabels, rotation=0)
    plt.savefig("crime-type-trends-png/Mischief.png")

    plt.figure(figsize=(9, 6))
    plt.title("Monthly Assault Rates")
    plt.xlabel("Month")
    plt.ylabel("# of Crimes")
    df_assault = df[df["TYPE"] == "Assault"].groupby(["YEAR","MONTH"]).size()
    df_assault = df_assault.groupby("MONTH").mean()
    df_assault.plot(marker="o", linestyle="-", color="blue")
    plt.xticks(xlabels, rotation=0)
    plt.savefig("crime-type-trends-png/Assault.png")

    plt.figure(figsize=(9, 6))
    plt.title("Monthly Theft Rates")
    plt.xlabel("Month")
    plt.ylabel("# of Crimes")
    df_theft = (
        df[(df["TYPE"] == "Theft-O") | (df["TYPE"] == "Theft-FV")].groupby(["YEAR","MONTH"]).size()
    )
    df_theft = df_theft.groupby("MONTH").mean()
    df_theft.plot(marker="o", linestyle="-", color="blue")
    plt.xticks(xlabels, rotation=0)
    plt.savefig("crime-type-trends-png/Theft.png")

    plt.figure(figsize=(9, 6))
    plt.title("Monthly Theft of Bike Rates")
    plt.xlabel("Month")
    plt.ylabel("# of Crimes")
    df_theft_OB = df[df["TYPE"] == "Theft-OB"].groupby(["YEAR","MONTH"]).size()
    df_theft_OB = df_theft_OB.groupby("MONTH").mean()
    df_theft_OB.plot(marker="o", linestyle="-", color="blue")
    plt.xticks(xlabels, rotation=0)
    plt.savefig("crime-type-trends-png/Theft-OB.png")

    plt.figure(figsize=(9, 6))
    plt.title("Monthly Theft of Vehicle Rates")
    plt.xlabel("Month")
    plt.ylabel("# of Crimes")
    df_theft_OV = df[df["TYPE"] == "Theft-OV"].groupby(["YEAR","MONTH"]).size()
    df_theft_OV = df_theft_OV.groupby("MONTH").mean()
    df_theft_OV.plot(marker="o", linestyle="-", color="blue")
    plt.xticks(xlabels, rotation=0)
    plt.savefig("crime-type-trends-png/Theft-OV.png")

    plt.figure(figsize=(9, 6))
    plt.title("Monthly Car Crash Rates")
    plt.xlabel("Month")
    plt.ylabel("# of Crimes")
    df_CC = df[(df["TYPE"] == "CC-F") | (df["TYPE"] == "CC-I")].groupby(["YEAR","MONTH"]).size()
    df_CC = df_CC.groupby("MONTH").mean()
    df_CC.plot(marker="o", linestyle="-", color="blue")
    plt.xticks(rotation=0)
    plt.savefig("crime-type-trends-png/CC.png")


def plot_monthly_crime_types(index, month):
    plt.figure(figsize=(9, 6))
    plt.title(f"Crime Types in {month}")
    plt.xlabel("Crime Type")
    plt.ylabel("# of Crimes")
    plt.ylim(0, 1100)
    monthly_df = df[df["MONTH"] == index]
    monthly_df = monthly_df.groupby(["YEAR", "TYPE"]).size()
    monthly_df = monthly_df.groupby("TYPE").mean()
    monthly_df.plot(kind="bar")
    plt.xticks(rotation=0)
    plt.savefig(f"monthly-crimes-png/{month}-crimes.png")

def monthly_crime_types():
    for index, month in enumerate(months):
        plot_monthly_crime_types(index + 1, month)
        

def create_monthly_neigbourhood_tables(index, month):
    monthly_df = df[df["MONTH"] == index]
    monthly_df = monthly_df.groupby(["YEAR","NEIGHBOURHOOD", "TYPE"]).size().to_frame("SIZE")
    monthly_df = monthly_df.reset_index()
    monthly_counts = pd.pivot_table(
        monthly_df[["NEIGHBOURHOOD", "TYPE", "SIZE"]],
        index="NEIGHBOURHOOD",
        columns="TYPE",
        fill_value=0,
    )
    monthly_counts.columns = monthly_counts.columns.droplevel(0)
    monthly_counts = monthly_counts.reset_index()
    monthly_counts.to_csv(f"data/neighbourhood-data/{month}-counts.csv", index=False)

def monthly_neighbourhood_crimes():
    for index, month in enumerate(months):
        create_monthly_neigbourhood_tables(index + 1, month)


def main():
    crime_rate_trends()
    monthly_crime_rate()
    crime_type_trends()
    monthly_crime_types()
    monthly_neighbourhood_crimes()


if __name__ == "__main__":
    main()
