import os
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# loading cleaned data
cleaned_files = [file for file in os.listdir("data/cleaned-data/")]

df = pd.DataFrame()
for file in cleaned_files:
    data = pd.read_csv("data/cleaned-data/" + file)
    df = pd.concat([df, data])

# Monthly DataFrames
num_of_years = df["YEAR"].max() - df["YEAR"].min() + 1

months = {
    "jan": "January",
    "feb": "February",
    "mar": "March",
    "apr": "April",
    "may": "May",
    "jun": "June",
    "jul": "July",
    "aug": "August",
    "sep": "September",
    "oct": "October",
    "nov": "November",
    "dec": "December",
}

seasons = ["winter", "spring", "summer", "fall"]


def crime_rate_trends():
    df["DATE"] = pd.to_datetime(
        df["YEAR"].astype(str) + df["MONTH"].astype(str), format="%Y%m"
    )
    plt.figure(figsize=(12, 8))
    plt.ylabel("Number of Crimes")
    plt.xlabel("DATE")
    plt.title("Crime Rate Trends")
    crime_rates = df.groupby("DATE").size()
    crime_rates.plot(marker="o", linestyle="-", color="blue")
    plt.savefig("crime-rate-trends.png")


def monthly_crime_rate():
    month_names = [month.capitalize() for month in months.keys()]
    monthly_crime = df.groupby(["YEAR", "MONTH"]).size()
    monthly_crime = monthly_crime.groupby("MONTH").mean()
    plt.figure(figsize=(12, 9))
    monthly_crime.plot(marker="o", linestyle="-", color="blue")
    plt.title("Monthly Crime Trends")
    plt.xlabel("Month")
    plt.ylabel("Number of Crimes")
    plt.xticks(range(1, len(month_names) + 1), month_names)
    plt.savefig("monthly-trends.png")


def crime_type_trends():
    xlabels = np.arange(1, 13)

    plt.figure(figsize=(9, 6))
    plt.title("Monthly Break & Enter Rates")
    plt.xlabel("Month")
    plt.ylabel("Number of Crimes")
    df_BE = (
        df[(df["TYPE"] == "B&E-C") | (df["TYPE"] == "B&E-R/O")]
        .groupby(["YEAR", "MONTH"])
        .size()
    )
    df_BE = df_BE.groupby("MONTH").mean()
    df_BE.plot(marker="o", linestyle="-", color="blue")
    plt.xticks(xlabels, rotation=0)
    plt.savefig("crime-type-trends-png/B&E.png")

    plt.figure(figsize=(9, 6))
    plt.title("Monthly Homicide Rates")
    plt.xlabel("Month")
    plt.ylabel("Number of Crimes")
    df_homicide = df[df["TYPE"] == "Homicide"].groupby(["YEAR", "MONTH"]).size()
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
    plt.ylabel("Number of Crimes")
    df_mischief = df[df["TYPE"] == "Mischief"].groupby(["YEAR", "MONTH"]).size()
    df_mischief = df_mischief.groupby("MONTH").mean()
    df_mischief.plot(marker="o", linestyle="-", color="blue")
    plt.xticks(xlabels, rotation=0)
    plt.savefig("crime-type-trends-png/Mischief.png")

    plt.figure(figsize=(9, 6))
    plt.title("Monthly Assault Rates")
    plt.xlabel("Month")
    plt.ylabel("Number of Crimes")
    df_assault = df[df["TYPE"] == "Assault"].groupby(["YEAR", "MONTH"]).size()
    df_assault = df_assault.groupby("MONTH").mean()
    df_assault.plot(marker="o", linestyle="-", color="blue")
    plt.xticks(xlabels, rotation=0)
    plt.savefig("crime-type-trends-png/Assault.png")

    plt.figure(figsize=(9, 6))
    plt.title("Monthly Theft Rates")
    plt.xlabel("Month")
    plt.ylabel("Number of Crimes")
    df_theft = (
        df[(df["TYPE"] == "Theft-O") | (df["TYPE"] == "Theft-FV")]
        .groupby(["YEAR", "MONTH"])
        .size()
    )
    df_theft = df_theft.groupby("MONTH").mean()
    df_theft.plot(marker="o", linestyle="-", color="blue")
    plt.xticks(xlabels, rotation=0)
    plt.savefig("crime-type-trends-png/Theft.png")

    plt.figure(figsize=(9, 6))
    plt.title("Monthly Theft of Bike Rates")
    plt.xlabel("Month")
    plt.ylabel("Number of Crimes")
    df_theft_OB = df[df["TYPE"] == "Theft-OB"].groupby(["YEAR", "MONTH"]).size()
    df_theft_OB = df_theft_OB.groupby("MONTH").mean()
    df_theft_OB.plot(marker="o", linestyle="-", color="blue")
    plt.xticks(xlabels, rotation=0)
    plt.savefig("crime-type-trends-png/Theft-OB.png")

    plt.figure(figsize=(9, 6))
    plt.title("Monthly Theft of Vehicle Rates")
    plt.xlabel("Month")
    plt.ylabel("Number of Crimes")
    df_theft_OV = df[df["TYPE"] == "Theft-OV"].groupby(["YEAR", "MONTH"]).size()
    df_theft_OV = df_theft_OV.groupby("MONTH").mean()
    df_theft_OV.plot(marker="o", linestyle="-", color="blue")
    plt.xticks(xlabels, rotation=0)
    plt.savefig("crime-type-trends-png/Theft-OV.png")

    plt.figure(figsize=(9, 6))
    plt.title("Monthly Car Crash Rates")
    plt.xlabel("Month")
    plt.ylabel("Number of Crimes")
    df_CC = (
        df[(df["TYPE"] == "CC-F") | (df["TYPE"] == "CC-I")]
        .groupby(["YEAR", "MONTH"])
        .size()
    )
    df_CC = df_CC.groupby("MONTH").mean()
    df_CC.plot(marker="o", linestyle="-", color="blue")
    plt.xticks(rotation=0)
    plt.savefig("crime-type-trends-png/CC.png")


def plot_seasonal_crime_types(season):
    plt.figure(figsize=(9, 6))
    plt.title(f"Crime Types in {season.capitalize()}")
    plt.xlabel("Crime Type")
    plt.ylabel("Number of Crimes")
    plt.ylim(0, 3100)
    seasonal_df = df[df["SEASON"] == season.capitalize()]
    seasonal_df = seasonal_df.groupby(["YEAR", "TYPE"]).size()
    seasonal_df = seasonal_df.groupby("TYPE").mean()
    seasonal_df.plot(kind="bar")
    plt.xticks(rotation=0)
    plt.savefig(f"seasonal-crimes-png/{season}-crimes.png")


def seasonal_crime_types():
    for season in seasons:
        plot_seasonal_crime_types(season)


def plot_monthly_crime_types(index, month_short, month_full):
    plt.figure(figsize=(9, 6))
    plt.title(f"Crime Types in {month_full}")
    plt.xlabel("Crime Type")
    plt.ylabel("Number of Crimes")
    plt.ylim(0, 1100)
    monthly_df = df[df["MONTH"] == index]
    monthly_df = monthly_df.groupby(["YEAR", "TYPE"]).size()
    monthly_df = monthly_df.groupby("TYPE").mean()
    monthly_df.plot(kind="bar")
    plt.xticks(rotation=0)
    plt.savefig(f"monthly-crimes-png/{month_short}-crimes.png")
    plt.close()


def monthly_crime_types():
    for index, (month_short, month_full) in enumerate(months.items()):
        plot_monthly_crime_types(index + 1, month_short, month_full)


def plot_seasonal_neighbourhood_crime_rates(season):
    fig, ax = plt.subplots(figsize=(16, 9))
    colormap = plt.cm.nipy_spectral
    colors = colormap(np.linspace(0, 1, 23))
    ax.set_prop_cycle("color", colors)
    plt.title(f"{season.capitalize()} Neighbourhood Crime Rates by Crime Type")
    plt.xlabel("Crime Type")
    plt.ylabel("Number of Crimes")
    plt.ylim(0, 900)
    df = pd.read_csv(f"data/neighbourhood-data/{season}-counts.csv")
    df = df.transpose()
    xlabels = df.index[1:]
    new_header = df.iloc[0]
    df = df[1:]
    df.columns = new_header
    df.plot(marker="o", linestyle="-", ax=ax, lw=1)
    plt.legend()
    plt.xticks(ticks=np.arange(11), labels=xlabels)
    plt.savefig(
        f"seasonal-neighbourhood-crime-rates-png/{season}-neighbourhood-crime-rates.png"
    )


def create_seasonal_neigbourhood_tables(season):
    seasonal_df = df[df["SEASON"] == season.capitalize()]
    seasonal_df = (
        seasonal_df.groupby(["YEAR", "NEIGHBOURHOOD", "TYPE"]).size().to_frame("SIZE")
    )
    seasonal_df = seasonal_df.reset_index()
    seasonal_counts = pd.pivot_table(
        seasonal_df[["NEIGHBOURHOOD", "TYPE", "SIZE"]],
        index="NEIGHBOURHOOD",
        columns="TYPE",
        fill_value=0,
    )
    seasonal_counts.columns = seasonal_counts.columns.droplevel(0)
    seasonal_counts = seasonal_counts.reset_index()
    seasonal_counts.to_csv(f"data/neighbourhood-data/{season}-counts.csv", index=False)


def seasonal_neighbourhood_crimes():
    for season in seasons:
        create_seasonal_neigbourhood_tables(season)
        plot_seasonal_neighbourhood_crime_rates(season)


def plot_seasonal_neighbourhood_cr(season):
    plt.figure(figsize=(12, 6))
    plt.title(f"Neighbourhood Crime Rate in {season.capitalize()}")
    plt.xlabel("Neighbourhood")
    plt.ylabel("Number of Crimes")
    plt.ylim(0, 3000)
    seasonal_df = df[df["SEASON"] == season.capitalize()]
    seasonal_df = seasonal_df.groupby(["YEAR", "NEIGHBOURHOOD"]).size()
    seasonal_df = seasonal_df.groupby("NEIGHBOURHOOD").mean()
    seasonal_df.plot(kind="bar")
    plt.xticks(rotation=0)
    plt.savefig(f"neighbourhood-seasonal-crime-rate-png/{season}-crime-rate.png")


def seasonal_neighbourhood_crime_rate():
    for season in seasons:
        plot_seasonal_neighbourhood_cr(season)


def main():
    crime_rate_trends()
    monthly_crime_rate()
    crime_type_trends()
    seasonal_crime_types()
    monthly_crime_types()
    seasonal_neighbourhood_crimes()
    seasonal_neighbourhood_crime_rate()


if __name__ == "__main__":
    main()
