import pandas as pd
import csv

df=pd.read_csv("data/Grand_Rapids_Bus_Stops.csv")
coord_list = ["LATITUDE","LONGITUDE"]

df_cleaned = df.dropna(subset=coord_list)
coords = df_cleaned[coord_list]
coord_arr = coords.values.tolist()

with open('data/coords.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerows(coord_arr)



