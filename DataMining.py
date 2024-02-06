import pandas as pd
import csv

'''
coord_list = ["LATITUDE","LONGITUDE"]
bus_df=pd.read_csv("data/Grand_Rapids_Bus_Stops.csv")

bus_df_cleaned = bus_df.dropna(subset=coord_list)
bus_coords = bus_df_cleaned[coord_list]
bus_coord_arr = bus_coords.values.tolist()

with open('data/bus_cleaned_coords.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerows(bus_coord_arr)
'''



'''
coord_list = ["Y", "X"]
protestant_df = pd.read_csv("data/protestant_churches.csv")

protestant_df_cleaned = protestant_df.dropna(subset=coord_list)
protestant_coords = protestant_df_cleaned[coord_list]
protestant_coord_arr = protestant_coords.values.tolist()

with open('data/protestant_cleaned_coords.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerows(protestant_coord_arr)
'''



'''
coord_list = ["latitude", "longitude"]
school_df = pd.read_csv("data/school_messy_coords.csv")

school_df_cleaned = school_df.dropna(subset=coord_list)
school_coords = school_df_cleaned[coord_list]
school_coord_arr = school_coords.values.tolist()

with open('data/school_cleaned_coords.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerows(school_coord_arr)
'''


# chat gpt definitely helped on this one. kml files are weird
import xml.etree.ElementTree as ET


def extract_coordinates_from_kml(kml_file):
    tree = ET.parse(kml_file)
    root = tree.getroot()

    # Namespace dictionary for KML
    ns = {'kml': 'http://www.opengis.net/kml/2.2'}

    # Find all coordinates within the KML file
    coordinates = root.findall('.//kml:coordinates', namespaces=ns)

    # Extracting longitude and latitude from each coordinate entry
    all_coordinates = []
    for coord_elem in coordinates:
        coords = coord_elem.text.strip().split()
        for coord in coords:
            longitude, latitude, _ = coord.split(',')
            all_coordinates.append((float(latitude), float(longitude)))

    return all_coordinates


def write_coordinates_to_csv(coordinates, csv_file):
    with open(csv_file, 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(['Latitude', 'Longitude'])  # Write header
        writer.writerows(coordinates)

# Example usage:
kml_file_path = 'data/Restaurants.kml'
csv_file_path = 'data/restaurant_cleaned_coords.csv'

coordinates = extract_coordinates_from_kml(kml_file_path)
write_coordinates_to_csv(coordinates, csv_file_path)
