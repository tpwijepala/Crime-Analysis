import pandas as pd
import sys
import folium
from folium import plugins
import webbrowser

cleaned_data_file = "data/cleaned-data/2022_crimedata.csv"

df = pd.read_csv(cleaned_data_file)

df = df.dropna()

mapWinter = folium.Map(location=[49.234696136718895,-123.16003300562792], zoom_start=10)
location = []
for index, row in df.iterrows():
        if row['MONTH']==12 or row['MONTH']==1:
                location.append([row['LAT'], row['LON']])
mapWinter.add_child(plugins.HeatMap(location, blur=24))

mapSummer = folium.Map(location=[49.234696136718895,-123.16003300562792], zoom_start=10)
location = []
for index, row in df.iterrows():
        if row['MONTH']>=6 and row['MONTH']<=8:
                location.append([row['LAT'], row['LON']])
mapSummer.add_child(plugins.HeatMap(location, blur=24))

mapWinter.save('mapwinter.html')
mapSummer.save('mapsummmer.html')
#webbrowser.open('map.html')