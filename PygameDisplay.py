import pygame
import ArrayBuilder
from GUI import Button

class DisplayMenu:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((1280, 720))
        pygame.display.set_caption("Menu")

        self.BLACK = (0, 0, 0)

        self.menu_font = pygame.font.SysFont('arial', 100)
        self.button_font = pygame.font.SysFont('arial', 75)
        self.play_button = Button(None, (640, 250), "Run Generator", self.button_font, (215, 252, 212), True)
        self.options_button = Button(None, (640, 400), "Options", self.button_font, (215, 252, 212), True)
        self.quit_button = Button(None, (640, 550), "Quit", self.button_font, (215, 252, 212), True)

        self.voronoi_selection = ArrayBuilder.build_schools()
        self.heat_map_check = True

        self.close_display = False
        self.main_menu()


    def main_menu(self):
        running = True
        while running:
            menu_mouse_pos = pygame.mouse.get_pos()

            self.screen.fill(self.BLACK)
            menu_text = self.menu_font.render("Voronoi Generator", True, (255, 255, 255))
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
                        running = False
                    elif self.options_button.checkForInput(event.pos):
                        self.options()
                    elif self.quit_button.checkForInput(event.pos):
                        pygame.quit()
                        quit()

            pygame.display.flip()

    def options(self):
        options_back = Button(None, (640, 675), "Back", self.button_font, (215, 252, 212), True)
        choose_voronoi = Button(None, (640, 150), "Choose Seed Set", self.button_font, (215, 252, 212), True)

        if self.heat_map_check:
            heat_map_yes = Button(None, (500, 300), "Heatmap", self.button_font, (255, 255, 255), True)
            heat_map_no = Button(None, (800, 300), "Diagram", self.button_font, (215, 252, 212), True)
        else:
            heat_map_yes = Button(None, (500, 300), "Heatmap", self.button_font, (215, 252, 212), True)
            heat_map_no = Button(None, (800, 300), "Diagram", self.button_font, (255, 255, 255), True)

        while True:
            self.screen.fill(self.BLACK)
            options_mouse_pos = pygame.mouse.get_pos()

            options_text = self.menu_font.render("Options", True, (255, 255, 255))
            options_rect = options_text.get_rect(center=(640, 50))
            self.screen.blit(options_text, options_rect)

            options_back.update(self.screen)
            choose_voronoi.update(self.screen)
            heat_map_yes.update(self.screen)
            heat_map_no.update(self.screen)

            if self.heat_map_check:
                heat_map_yes = Button(None, (500, 300), "Heatmap", self.button_font, (255, 255, 255), True)
                heat_map_no = Button(None, (800, 300), "Diagram", self.button_font, (215, 252, 212), True)
            else:
                heat_map_yes = Button(None, (500, 300), "Heatmap", self.button_font, (215, 252, 212), True)
                heat_map_no = Button(None, (800, 300), "Diagram", self.button_font, (255, 255, 255), True)

            pygame.display.flip()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if options_back.checkForInput(options_mouse_pos):
                        return
                    elif choose_voronoi.checkForInput(options_mouse_pos):
                        self.choose_voronoi_screen()
                    elif heat_map_yes.checkForInput(options_mouse_pos):
                        self.heat_map_check = True
                    elif heat_map_no.checkForInput(options_mouse_pos):
                        self.heat_map_check = False

    def choose_voronoi_screen(self):
        voronoi_back = Button(None, (640, 675), "Back", self.button_font, (215, 252, 212), True)
        schools = Button(None, (25, 100), "Schools", self.button_font, (215, 252, 212), False)
        churches = Button(None, (25, 175), "Churches", self.button_font, (215, 252, 212), False)
        bus_stops = Button(None, (25, 250), "Bus Stops", self.button_font, (215, 252, 212), False)
        restaurants = Button(None, (25, 325), "Restaurants", self.button_font, (215, 252, 212), False)

        while True:
            self.screen.fill(self.BLACK)
            voronoi_mouse_pos = pygame.mouse.get_pos()

            voronoi_title = self.menu_font.render("Voronoi Seed Sets", True, (255, 255, 255))
            voronoi_rect = voronoi_title.get_rect(center=(640, 50))
            self.screen.blit(voronoi_title, voronoi_rect)

            voronoi_back.update(self.screen)
            schools.update(self.screen)
            churches.update(self.screen)
            bus_stops.update(self.screen)
            restaurants.update(self.screen)
            pygame.display.flip()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if voronoi_back.checkForInput(voronoi_mouse_pos):
                        return
                    elif schools.checkForInput(voronoi_mouse_pos):
                        self.voronoi_selection = ArrayBuilder.build_schools()
                    elif churches.checkForInput(voronoi_mouse_pos):
                        self.voronoi_selection = ArrayBuilder.build_protestant()
                    elif bus_stops.checkForInput(voronoi_mouse_pos):
                        self.voronoi_selection = ArrayBuilder.build_bus()
                    elif restaurants.checkForInput(voronoi_mouse_pos):
                        self.voronoi_selection = ArrayBuilder.build_restaurants()




if __name__ == "__main__":
    display = DisplayMenu()


'''
Pygame GUI Inspiration from https://github.com/baraltech/Menu-System-PyGame/tree/main
'''
