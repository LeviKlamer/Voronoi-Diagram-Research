import math

class Coords():
    def __init__(self, size):
        #  abstract numbers, change when defined
        self.max_lat = 43.096085  # Top left
        self.min_lat = 42.760639  # Bottom right
        self.min_long = -85.894024  # Top left
        self.max_long = -85.385939  # Bottom right
        self.size = size
        self.latlongs = []
        self.resized_coords = []

    def fix_coords(self, arr):
        # Applies min-max formula to each coord long/lat, multiplies by size for new matrix coords
        new_coord_arr = []
        for i in arr:
            new_coord = [0, 0]
            new_coord[0] = math.floor((1 - ((i[0] - self.min_lat) / (self.max_lat - self.min_lat))) * self.size)  # take the inverse because our axis is opposite of theirs
            new_coord[1] = math.floor((i[1] - self.min_long) / (self.max_long - self.min_long) * self.size)
            new_coord_arr.append(new_coord)

        return new_coord_arr

    def to_latlong(self, arr):
        # Does the opposite of the one above it
        latlong_arr = []
        for i in arr:
            new_coord = [0, 0]
            new_coord[0] = (i[0] / self.size) * (self.max_lat - self.min_lat) + self.min_lat
            new_coord[1] = (i[1] / self.size) * (self.max_long - self.min_long) + self.min_long

            latlong_arr.append(new_coord)

        return latlong_arr




'''bus_coords = Coords(2048)
bus_coords.latlongs = [[42.9626334737292, -85.6679353753174], [42.9597360004466, -85.6679609996548], [42.9580959999672, -85.6678699997781]]
print(f'OG lat/longs: {bus_coords.latlongs}')
print(f'conversion coords: {bus_coords.resized_coords}')
print(f'New lat/longs: {bus_coords.to_latlong(bus_coords.resized_coords)}')'''
