import pandas as pd
import sys
import folium
from folium import plugins
import webbrowser

cleaned_data_file = "data/cleaned-data/2022_crimedata.csv"

df = pd.read_csv(cleaned_data_file)

df = df.dropna()

map = folium.Map(location=[49.234696136718895,-123.16003300562792], zoom_start=10)
location = []
for index, row in df.iterrows():
        location.append([row['LAT'], row['LON']])
map.add_child(plugins.HeatMap(location, blur=32))

map.save('map.html')
webbrowser.open('map.html')