import pygame
import ArrayBuilder
from GUI import Button

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (215, 252, 212)

class DisplayMenu:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((1280, 720))
        pygame.display.set_caption("Voronoi Generator")

        self.BLACK = (0, 0, 0)

        self.menu_font = pygame.font.SysFont('arial', 100)
        self.button_font = pygame.font.SysFont('arial', 75)

        self.voronoi_selection = "Schools"
        self.heat_map_check = True

        self.close_display = False
        self.buttons_init()
        self.main_menu()

    def buttons_init(self):
        self.play_button = Button(None, (640, 250), "Run Generator", self.button_font, GREEN, True)
        self.options_button = Button(None, (640, 400), "Options", self.button_font, GREEN, True)
        self.quit_button = Button(None, (640, 550), "Quit", self.button_font, GREEN, True)

        self.options_back = Button(None, (640, 675), "Back", self.button_font, GREEN, True)
        self.choose_voronoi = Button(None, (640, 150), "Choose Seed Set", self.button_font, GREEN, True)

        self.heat_map_yes = Button(None, (500, 300), "Heatmap", self.button_font, WHITE, True)
        self.heat_map_no = Button(None, (800, 300), "Diagram", self.button_font, GREEN, True)

        self.voronoi_back = Button(None, (640, 675), "Back", self.button_font, WHITE, True)
        self.schools = Button(None, (25, 100), "Schools", self.button_font, WHITE, False)
        self.churches = Button(None, (25, 175), "Churches", self.button_font, GREEN, False)
        self.bus_stops = Button(None, (25, 250), "Bus Stops", self.button_font, GREEN, False)
        self.restaurants = Button(None, (25, 325), "Restaurants", self.button_font, GREEN, False)
        self.seed_sets = [self.voronoi_back, self.schools, self.churches, self.bus_stops, self.restaurants]

    def update_heatmap(self):
        if self.heat_map_check:
            self.heat_map_yes.color = WHITE
            self.heat_map_no.color = GREEN
        else:
            self.heat_map_yes.color = GREEN
            self.heat_map_no.color = WHITE

    def update_seed_set(self, selection):
        for i in self.seed_sets:
            if i == selection:
                i.color = WHITE
            else:
                i.color = GREEN


    def main_menu(self):
        running = True
        while running:

            self.screen.fill(self.BLACK)
            menu_text = self.menu_font.render("Voronoi Generator", True, WHITE)
            menu_rect = menu_text.get_rect(center=(640, 100))
            self.screen.blit(menu_text, menu_rect)

            self.play_button.update(self.screen)
            self.options_button.update(self.screen)
            self.quit_button.update(self.screen)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if self.play_button.checkForInput(event.pos):
                        loading_text = self.menu_font.render("Loading...", True, WHITE)
                        loading_rect = loading_text.get_rect(center=(200, 650))
                        self.screen.blit(loading_text, loading_rect)
                        running = False
                    elif self.options_button.checkForInput(event.pos):
                        self.options()
                    elif self.quit_button.checkForInput(event.pos):
                        pygame.quit()
                        quit()

            pygame.display.flip()


    def options(self):
        self.update_heatmap()
        while True:
            self.screen.fill(self.BLACK)

            options_text = self.menu_font.render("Options", True, WHITE)
            options_rect = options_text.get_rect(center=(640, 50))
            self.screen.blit(options_text, options_rect)

            self.options_back.update(self.screen)
            self.choose_voronoi.update(self.screen)
            self.heat_map_yes.update(self.screen)
            self.heat_map_no.update(self.screen)

            pygame.display.flip()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if self.options_back.checkForInput(event.pos):
                        return
                    elif self.choose_voronoi.checkForInput(event.pos):
                        self.choose_voronoi_screen()
                    elif self.heat_map_yes.checkForInput(event.pos):
                        self.heat_map_check = True
                        self.update_heatmap()
                    elif self.heat_map_no.checkForInput(event.pos):
                        self.heat_map_check = False
                        self.update_heatmap()


    def choose_voronoi_screen(self):

        while True:
            self.screen.fill(self.BLACK)

            voronoi_title = self.menu_font.render("Voronoi Seed Sets", True, (255, 255, 255))
            voronoi_rect = voronoi_title.get_rect(center=(640, 50))
            self.screen.blit(voronoi_title, voronoi_rect)

            self.voronoi_back.update(self.screen)
            self.schools.update(self.screen)
            self.churches.update(self.screen)
            self.bus_stops.update(self.screen)
            self.restaurants.update(self.screen)
            pygame.display.flip()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if self.voronoi_back.checkForInput(event.pos):
                        return
                    elif self.schools.checkForInput(event.pos):
                        self.update_seed_set(self.schools)
                        self.voronoi_selection = self.schools.text_input
                    elif self.churches.checkForInput(event.pos):
                        self.update_seed_set(self.churches)
                        self.voronoi_selection = self.churches.text_input
                    elif self.bus_stops.checkForInput(event.pos):
                        self.update_seed_set(self.bus_stops)
                        self.voronoi_selection = self.bus_stops.text_input
                    elif self.restaurants.checkForInput(event.pos):
                        self.update_seed_set(self.restaurants)
                        self.voronoi_selection = self.restaurants.text_input




if __name__ == "__main__":
    display = DisplayMenu()


'''
Pygame GUI Inspiration from https://github.com/baraltech/Menu-System-PyGame/tree/main
'''
