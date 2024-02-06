import time
import random
import pygame
from CoordBuilder import Coords
from numba import jit, njit
import numpy as np
import ArrayBuilder
# import csv


@njit
def find_closest_seed(p, array_of_seeds):
    n = len(array_of_seeds)
    closest_seed = -1
    shortest_distance = np.inf

    for i in range(int(n / 2)):
        distance_to_this_seed = (p[0] - int(array_of_seeds[2 * i + 0])) ** 2 + (
                    p[1] - int(array_of_seeds[2 * i + 1])) ** 2
        if distance_to_this_seed < shortest_distance:
            closest_seed = i
            shortest_distance = distance_to_this_seed

    return closest_seed


@njit
def fill_area(canvas, size, p1, p2, p3, p4, color):
    for i in range(p1[0], p2[0] + 1):
        for j in range(p1[1], p4[1] + 1):
            canvas[j * size + i] = color


@njit
def recursive_quad(canvas, size, p1, p2, p3, p4, array_of_seeds=np.array([])):
    closestSeedP1 = find_closest_seed(p1, array_of_seeds)
    closestSeedP2 = find_closest_seed(p2, array_of_seeds)
    closestSeedP3 = find_closest_seed(p3, array_of_seeds)
    closestSeedP4 = find_closest_seed(p4, array_of_seeds)

    if (closestSeedP1 == closestSeedP2) and (closestSeedP2 == closestSeedP3) and (closestSeedP3 == closestSeedP4):
        fill_area(canvas, size, p1, p2, p3, p4, closestSeedP1)
    else:
        middlePointX = (p1[0] + p2[0]) // 2
        middlePointY = (p1[1] + p4[1]) // 2

        quad1p1 = p1
        quad1p2 = (middlePointX, p1[1])
        quad1p3 = (middlePointX, middlePointY)
        quad1p4 = (p1[0], middlePointY)

        quad2p1 = (middlePointX + 1, p1[1])
        quad2p2 = p2
        quad2p3 = (p2[0], middlePointY)
        quad2p4 = (middlePointX + 1, middlePointY)

        quad3p1 = (middlePointX + 1, middlePointY + 1)
        quad3p2 = (p2[0], middlePointY + 1)
        quad3p3 = p3
        quad3p4 = (middlePointX + 1, p3[1])

        quad4p1 = (p1[0], middlePointY + 1)
        quad4p2 = (middlePointX, middlePointY + 1)
        quad4p3 = (middlePointX, p4[1])
        quad4p4 = p4

        recursive_quad(canvas, size, quad1p1, quad1p2, quad1p3, quad1p4, array_of_seeds)
        recursive_quad(canvas, size, quad2p1, quad2p2, quad2p3, quad2p4, array_of_seeds)
        recursive_quad(canvas, size, quad3p1, quad3p2, quad3p3, quad3p4, array_of_seeds)
        recursive_quad(canvas, size, quad4p1, quad4p2, quad4p3, quad4p4, array_of_seeds)


class VoronoiGenerator:
    def __init__(self, arr_of_coords):
        self.array_of_seeds = []
        self.size = 2048
        self.array_of_seeds = np.array(self.array_of_seeds, dtype=np.float64)
        self.canvas_original = [-1] * (self.size * self.size)
        self.canvas = np.array(self.canvas_original, dtype=np.int32)
        self.colors = []
        self.coords = Coords(self.size)

        self.coords.latlongs = arr_of_coords
        self.n = len(self.coords.latlongs)

        # Add a custom color for each seed
        for _ in self.coords.latlongs:
            self.colors.append((random.randint(0, 175), random.randint(0, 175), random.randint(0, 175)))

        # There's probably a less gross way of calling this
        self.coords.resized_coords = self.coords.fix_coords(self.coords.latlongs)
        print(self.coords.resized_coords)

        for i in self.coords.resized_coords:
            self.array_of_seeds = np.append(self.array_of_seeds, [[i[0], i[1]]], axis=None)

    def generate_voronoi(self):
        p1 = np.array([0, 0], dtype=np.int32)
        p2 = np.array([self.size - 1, 0], dtype=np.int32)
        p3 = np.array([self.size - 1, self.size - 1], dtype=np.int32)
        p4 = np.array([0, self.size - 1], dtype=np.int32)

        start_time = time.time()

        recursive_quad(self.canvas, self.size, p1, p2, p3, p4, self.array_of_seeds)
        end_time = time.time()
        duration = (end_time - start_time) * 1000
        print(f"Time for quad tree Voronoi: {duration} milliseconds with {self.n} seeds.")  # Change to just milliseconds, easier to pipe into file

    def display_voronoi(self):
        pygame.init()
        window_size = (self.size / 2, self.size / 2)
        window = pygame.display.set_mode(window_size)
        dummy_surface = pygame.Surface((self.size, self.size))
        for i in range(self.size):
            for j in range(self.size):
                color = self.colors[self.canvas[j * self.size + i]]
                rect = pygame.Rect(i, j, 1, 1)
                pygame.draw.rect(dummy_surface, color, rect)

        # This labels every seed location with a white circle. This could easily be applied to mark various POI in Grand Rapids
        white = (255, 255, 255)
        radius = 5
        for seed in self.coords.resized_coords:
            pygame.draw.circle(dummy_surface, white, (seed[0], seed[1]), radius)

        pygame.display.update()

        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False

                # Give coordinates of mouse click
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    mouse_x, mouse_y = pygame.mouse.get_pos()
                    print(f"Mouse clicked at ({mouse_x * 2}, {mouse_y * 2})")

                    local_coords = [mouse_x*2, mouse_y*2]
                    print(f"Coordinates: {self.coords.to_latlong_1D(local_coords)}")

            # Scale the 2048x2048 surface down to preferred screen viewing, then display the new surface
            scaled_surface = pygame.transform.scale(dummy_surface, window_size)
            window.blit(scaled_surface, (0, 0))
            pygame.display.update()

        pygame.quit()


def main():
    # bus_stop_coords = ArrayBuilder.build_bus()
    # protestant_coords = ArrayBuilder.build_protestant()
    school_coords = ArrayBuilder.build_schools()
    # restaurant_coords = ArrayBuilder.build_restaurants()

    hospital_coords = [[42.97064682743409, -85.66608871623687], [42.94424606653896, -85.55830002184193], [42.963471500540415, -85.66624111127469], [42.950680440861895, -85.5606616812743],
                       [43.01559138589651, -85.71960201023141], [42.89066585258278, -85.76713512360661], [42.958811064761186, -85.66236868254477], [42.97070084999957, -85.66476558145712],
                       [42.95378686333377, -85.62298869532792], [42.95367076159726, -85.6232751217235], [42.86027044244486, -85.71607368189366], [42.856100851064355, -85.76503446041109], [42.883621600674694, -85.62107965807779]]

    debug = [[43.09608, -85.89402], [42.76063, -85.89402]]

    generator = VoronoiGenerator(school_coords)

    print("While Compiling:")
    generator.generate_voronoi()
    print("Already Compiled:")
    generator.generate_voronoi()

    generator.display_voronoi()


if __name__ == "__main__":
    main()
