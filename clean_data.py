import sys
import pandas as pd

# input_file = sys.argv[1]

#temp file name
input_file = 'data/2022-data/crimedata_csv_AllNeighbourhoods_2022.csv'
df = pd.read_csv(input_file)

df = df.drop(['DAY', 'HOUR', 'MINUTE', 'HUNDRED_BLOCK', 'X', 'Y'], axis=1)

df_categories = df['TYPE'].unique()
print(df_categories)

rename_mapping = {'Break and Enter Commercial':'B&E-C', 'Break and Enter Residential/Other':'B&E-R/O',
                  'Homicide':'Homicide','Mischief':'Mischief' ,'Offence Against a Person':'Assult', 
                  'Other Theft':'Theft-O', 'Theft from Vehicle':'Theft-FV', 'Theft of Bicycle':'Theft-OB', 'Theft of Vehicle':'Theft-OV',
                  'Vehicle Collision or Pedestrian Struck (with Fatality)':'CC-F', 'Vehicle Collision or Pedestrian Struck (with Injury)':'CF-I'}
df['TYPE'] = df['TYPE'].map(rename_mapping)

df_categories_new = df['TYPE'].unique()
print(df_categories_new)

""" Note that some crimes are similiar:
B&E Commerical & B&E res/other,
Theft From Vehicle, Theft of Bicycle & Theft of Vehicle,
Car Crash (w/ Fatality), Car Crash (w/ Injury)

Will need to take into account the similiarities/Differences when analyzing data"""

print(df)