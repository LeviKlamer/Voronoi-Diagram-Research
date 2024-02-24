class Button:
    def __init__(self, image, pos, text_input, font, color, centered):
        self.image = image
        self.x_pos = pos[0]
        self.y_pos = pos[1]
        self.font = font
        self.color = color
        self.text_input = text_input
        self.text = self.font.render(self.text_input, True, self.color)
        if self.image is None:
            self.image = self.text
        if centered:
            self.rect = self.image.get_rect(center=(self.x_pos, self.y_pos))
            self.text_rect = self.text.get_rect(center=(self.x_pos, self.y_pos))
        else:
            self.rect = self.image.get_rect()
            self.rect.x, self.rect.y = self.x_pos, self.y_pos
            self.text_rect = self.text.get_rect()
            self.text_rect.x, self.text_rect.y = self.x_pos, self.y_pos

    def update(self, screen):
        self.text = self.font.render(self.text_input, True, self.color)

        if self.image is not None:
            screen.blit(self.image, self.rect)

        screen.blit(self.text, self.text_rect)

    def checkForInput(self, position):
        if position[0] in range(self.rect.left, self.rect.right) and position[1] in range(self.rect.top, self.rect.bottom):
            return True
        return False

'''
Pygame GUI Inspiration from https://github.com/baraltech/Menu-System-PyGame/tree/main
'''
