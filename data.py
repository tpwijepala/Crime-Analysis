import sys
import pandas as pd

# input_file = sys.argv[1]

input_file = 'data/2022-data/crimedata_csv_AllNeighbourhoods_2022.csv'
df = pd.read_csv(input_file)
df = df['TYPE']
print(df)