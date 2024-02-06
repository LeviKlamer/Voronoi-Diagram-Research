import csv


def build_bus():
    bus_stop_coords = []

    with open('data/bus_cleaned_coords.csv', 'r') as file:
        reader = csv.reader(file)
        for row in reader:
            bus_stop_coords.append([float(value) for value in row])

    return bus_stop_coords


def build_protestant():
    protestant_coords = []

    with open('data/protestant_cleaned_coords.csv', 'r') as file:
        reader = csv.reader(file)

        for row in reader:
            protestant_coords.append([float(value) for value in row])

    return protestant_coords


def build_schools():
    school_coords = []

    with open('data/school_cleaned_coords.csv', 'r') as file:
        reader = csv.reader(file)

        for row in reader:
            school_coords.append([float(value) for value in row])

    return school_coords

def build_restaurants():
    restaurant_coords = []

    with open('data/restaurant_cleaned_coords.csv', 'r') as file:
        reader = csv.reader(file)

        for row in reader:
            restaurant_coords.append([float(value) for value in row])

    return restaurant_coords
