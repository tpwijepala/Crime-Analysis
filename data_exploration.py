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

def monthly_trends(df):
    # Exploring monthly trends in crimes
    monthly_crime = df.groupby("MONTH").size()
    plt.figure(figsize=(12,8))
    monthly_crime.plot(marker="o", linestyle="-", color="blue")
    plt.title("Monthly Crime Trends")
    plt.xlabel("Month")
    plt.ylabel("Number of Crimes")

def monthly_crime_types():
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

def monthly_neighbourhood_crimes():
    jan_counts = pd.pivot_table(df_jan[["NEIGHBOURHOOD", "TYPE", "MONTH"]], index = "NEIGHBOURHOOD", columns="TYPE", aggfunc="count", fill_value=0)
    jan_counts.columns = jan_counts.columns.droplevel(0)
    jan_counts = jan_counts.reset_index() 
    jan_counts.to_csv("data/neighbourhood-data/jan-counts.csv", index=False)
    
    feb_counts = pd.pivot_table(df_feb[["NEIGHBOURHOOD", "TYPE", "MONTH"]], index = "NEIGHBOURHOOD", columns="TYPE", aggfunc="count", fill_value=0)
    feb_counts.columns = feb_counts.columns.droplevel(0)
    feb_counts = feb_counts.reset_index() 
    feb_counts.to_csv("data/neighbourhood-data/feb-counts.csv", index=False)
    
    mar_counts = pd.pivot_table(df_mar[["NEIGHBOURHOOD", "TYPE", "MONTH"]], index = "NEIGHBOURHOOD", columns="TYPE", aggfunc="count", fill_value=0)
    mar_counts.columns = mar_counts.columns.droplevel(0)
    mar_counts = mar_counts.reset_index() 
    mar_counts.to_csv("data/neighbourhood-data/mar-counts.csv", index=False)
    
    apr_counts = pd.pivot_table(df_apr[["NEIGHBOURHOOD", "TYPE", "MONTH"]], index = "NEIGHBOURHOOD", columns="TYPE", aggfunc="count", fill_value=0)
    apr_counts.columns = apr_counts.columns.droplevel(0)
    apr_counts = apr_counts.reset_index() 
    apr_counts.to_csv("data/neighbourhood-data/apr-counts.csv", index=False)
    
    may_counts = pd.pivot_table(df_may[["NEIGHBOURHOOD", "TYPE", "MONTH"]], index = "NEIGHBOURHOOD", columns="TYPE", aggfunc="count", fill_value=0)
    may_counts.columns = may_counts.columns.droplevel(0)
    may_counts = may_counts.reset_index() 
    may_counts.to_csv("data/neighbourhood-data/may-counts.csv", index=False)
    
    jun_counts = pd.pivot_table(df_jun[["NEIGHBOURHOOD", "TYPE", "MONTH"]], index = "NEIGHBOURHOOD", columns="TYPE", aggfunc="count", fill_value=0)
    jun_counts.columns = jun_counts.columns.droplevel(0)
    jun_counts = jun_counts.reset_index() 
    jun_counts.to_csv("data/neighbourhood-data/jun-counts.csv", index=False)
    
    jul_counts = pd.pivot_table(df_jul[["NEIGHBOURHOOD", "TYPE", "MONTH"]], index = "NEIGHBOURHOOD", columns="TYPE", aggfunc="count", fill_value=0)
    jul_counts.columns = jul_counts.columns.droplevel(0)
    jul_counts = jul_counts.reset_index() 
    jul_counts.to_csv("data/neighbourhood-data/jul-counts.csv", index=False)
    
    aug_counts = pd.pivot_table(df_aug[["NEIGHBOURHOOD", "TYPE", "MONTH"]], index = "NEIGHBOURHOOD", columns="TYPE", aggfunc="count", fill_value=0)
    aug_counts.columns = aug_counts.columns.droplevel(0)
    aug_counts = aug_counts.reset_index() 
    aug_counts.to_csv("data/neighbourhood-data/aug-counts.csv", index=False)
    
    sep_counts = pd.pivot_table(df_sep[["NEIGHBOURHOOD", "TYPE", "MONTH"]], index = "NEIGHBOURHOOD", columns="TYPE", aggfunc="count", fill_value=0)
    sep_counts.columns = sep_counts.columns.droplevel(0)
    sep_counts = sep_counts.reset_index() 
    sep_counts.to_csv("data/neighbourhood-data/sep-counts.csv", index=False)
    
    oct_counts = pd.pivot_table(df_oct[["NEIGHBOURHOOD", "TYPE", "MONTH"]], index = "NEIGHBOURHOOD", columns="TYPE", aggfunc="count", fill_value=0)
    oct_counts.columns = oct_counts.columns.droplevel(0)
    oct_counts = oct_counts.reset_index() 
    oct_counts.to_csv("data/neighbourhood-data/oct-counts.csv", index=False)
    
    nov_counts = pd.pivot_table(df_nov[["NEIGHBOURHOOD", "TYPE", "MONTH"]], index = "NEIGHBOURHOOD", columns="TYPE", aggfunc="count", fill_value=0)
    nov_counts.columns = nov_counts.columns.droplevel(0)
    nov_counts = nov_counts.reset_index() 
    nov_counts.to_csv("data/neighbourhood-data/nov-counts.csv", index=False)
    
    dec_counts = pd.pivot_table(df_dec[["NEIGHBOURHOOD", "TYPE", "MONTH"]], index = "NEIGHBOURHOOD", columns="TYPE", aggfunc="count", fill_value=0)
    dec_counts.columns = dec_counts.columns.droplevel(0)
    dec_counts = dec_counts.reset_index() 
    dec_counts.to_csv("data/neighbourhood-data/dev-counts.csv", index=False)

def main():
    monthly_trends(df)
    plt.savefig('monthly_trends.png')
    
    monthly_crime_types()
    plt.savefig('monthly_crime_types.png')
    
    monthly_neighbourhood_crimes()
    
main()