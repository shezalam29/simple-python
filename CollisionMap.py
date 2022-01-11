#Shezan Alam
#shezan.alam48@myhunter.cuny.edu

import folium
import pandas as pd 
n = input("Enter CSV file name: ")
o = input("Enter output file: ")

clsn = pd.read_csv(n)
mapNYC = folium.Map()

for index,row in clsn.iterrows():
        lat = row["LATITUDE"]
        lon = row["LONGITUDE"]
        name = row["TIME"]
        newMarker = folium.Marker([lat,lon], popup=name)
        newMarker.add_to(mapNYC)



mapNYC.save(outfile=o)
