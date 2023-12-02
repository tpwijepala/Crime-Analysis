import pandas as pd
import sys
import folium
import webbrowser

cleaned_data_file = "data/cleaned-data/2022_crimedata.csv"

df = pd.read_csv(cleaned_data_file)

df = df.dropna()

map = folium.Map(location=[49.234696136718895,-123.16003300562792], zoom_start=10)
for i, row in df.iterrows():
    if(str(row['YEAR'])=='2022' and str(row['TYPE'])=='Theft-OV'):
        print(row['YEAR'], row['TYPE'])
        folium.Marker(location=[row['LAT'], row['LON']],icon=folium.Icon(color="red")).add_to(map)

map.save('map.html')
webbrowser.open('map.html')
