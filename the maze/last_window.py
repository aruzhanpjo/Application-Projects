import pygame, sys
#from pygame_sample import *
class Button():
	def __init__(self, image, pos, text_input, font, base_color, hovering_color):
		self.image = image
		self.x_pos = pos[0]
		self.y_pos = pos[1]
		self.font = font
		self.base_color, self.hovering_color = base_color, hovering_color
		self.text_input = text_input
		self.text = self.font.render(self.text_input, True, self.base_color)
		if self.image is None:
			self.image = self.text
		self.rect = self.image.get_rect(center=(self.x_pos, self.y_pos))
		self.text_rect = self.text.get_rect(center=(self.x_pos, self.y_pos))

	def update(self, screen):
		if self.image is not None:
			screen.blit(self.image, self.rect)
		screen.blit(self.text, self.text_rect)

	def checkForInput(self, position):
		if position[0] in range(self.rect.left, self.rect.right) and position[1] in range(self.rect.top, self.rect.bottom):
			return True
		return False

	def changeColor(self, position):
		if position[0] in range(self.rect.left, self.rect.right) and position[1] in range(self.rect.top, self.rect.bottom):
			self.text = self.font.render(self.text_input, True, self.hovering_color)
		else:
			self.text = self.font.render(self.text_input, True, self.base_color)




#Command for initilization of pygame
pygame.init()

#For displaying the outline of the screen works as a base for the things we put after.
SCREEN = pygame.display.set_mode((1280, 720))
pygame.display.set_caption("Menu")

#Changes the background that is black to whatever we select.
BG = pygame.image.load("Background.png")

#Changes the font.
def get_font(size): # Returns Press-Start-2P in the desired size
    return pygame.font.Font("font.ttf", size)
    

def last_window():
    while True:
        SCREEN.blit(BG, (0, 0))

        LAST_MOUSE_POS = pygame.mouse.get_pos()

        LAST_TEXT = get_font(100).render("OOPS...", True, "#b68f40")
        LAST_RECT = LAST_TEXT.get_rect(center=(640, 100))

        TRY_BUTTON = Button(image=pygame.image.load("Play Rect.png"), pos=(640, 250), 
                            text_input="TRY AGAIN", font=get_font(75), base_color="#d7fcd4", hovering_color="White")
        QUIT_BUTTON = Button(image=pygame.image.load("Quit Rect.png"), pos=(640, 550), 
                            text_input="QUIT", font=get_font(75), base_color="#d7fcd4", hovering_color="White")

        SCREEN.blit(LAST_TEXT, LAST_RECT)

        for button in [TRY_BUTTON, QUIT_BUTTON]:
            button.changeColor(LAST_MOUSE_POS)
            button.update(SCREEN)
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if TRY_BUTTON.checkForInput(LAST_MOUSE_POS):
                    play()
                if QUIT_BUTTON.checkForInput(LAST_MOUSE_POS):
                    pygame.quit()
                    sys.exit()


        pygame.display.update()
