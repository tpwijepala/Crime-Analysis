import pandas as pd
import sys
import folium
from folium import plugins
import webbrowser

cleaned_data_file = "data/cleaned-data/2022_crimedata.csv"

df = pd.read_csv(cleaned_data_file)

df = df.dropna()



mapWinter = folium.Map(tiles="Cartodb Positron", location=[49.234696136718895,-123.16003300562792], zoom_start=10)

location = []
for index, row in df.iterrows():
        if row['MONTH']>=12 and row['MONTH']<=2:
                location.append([row['LAT'], row['LON']])
mapWinter.add_child(plugins.HeatMap(location, blur=14, min_opacity=0.25))

mapSummer = folium.Map(tiles="Cartodb Positron", location=[49.234696136718895,-123.16003300562792], zoom_start=10)
location = []
for index, row in df.iterrows():
        if row['MONTH']>=6 and row['MONTH']<=8:
                location.append([row['LAT'], row['LON']])
mapSummer.add_child(plugins.HeatMap(location, blur=14, min_opacity=0.25))

mapFall = folium.Map(tiles="Cartodb Positron", location=[49.234696136718895,-123.16003300562792], zoom_start=10)
location = []
for index, row in df.iterrows():
        if row['MONTH']>=9 and row['MONTH']<=11:
                location.append([row['LAT'], row['LON']])
mapFall.add_child(plugins.HeatMap(location, blur=14, min_opacity=0.25))

mapSpring = folium.Map(tiles="Cartodb Positron", location=[49.234696136718895,-123.16003300562792], zoom_start=10)
location = []
for index, row in df.iterrows():
        if row['MONTH']>=3 and row['MONTH']<=5:
                location.append([row['LAT'], row['LON']])
mapSpring.add_child(plugins.HeatMap(location, blur=14, min_opacity=0.25))

mapWinter.save('maps/mapwinter.html')
mapSummer.save('maps/mapsummmer.html')
mapFall.save('maps/mapfall.html')
mapSpring.save('maps/mapspring.html')
#webbrowser.open('map.html')