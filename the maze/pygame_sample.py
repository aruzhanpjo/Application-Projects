'''
Aruzhan Betigenova, Jihee Kim, Lakshman Bika, Adonai Lilay
Team #1

game is a maze, where a monkey chases banana & game ends whenever time ends or monkey reaches endpoint (banana)
April 20th, 2023




Rubric Lines:
1. Loops:
	line 133 (pygame_sample.py)
	line 131 (from maze_game003.py)
	
2. Nested Selection Statement:
	line 120 (pygame_sample.py)
	
3. I/O File:
	line 79-82 (maze_game003.py)
	
4. Collections:
	line 127-128 (maze_game003.py)
	line 153 (maze_game003.py)
	line 30 (maze_generator002.py)
	
5. Funcrions:
	line 57 (pygame_sample.py)
	line 88 (pygame_sample.py)
	line 148 (pygame_sample.py)
	
6. Classes:
	 line 49 (pygame_sample.py)
	 line 27 (maze_game003.py)
	 line 27 (maze_generator002.py)




Reference:
1. https://github.com/StanislavPetrovV/Maze_Game
2. https://www.youtube.com/watch?v=GMBqjxcKogA



'''


import pygame, sys
from maze_game003 import *




#Excecution of Buttons
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





pygame.init()
#For displaying the outline of the screen works as a base for the things we put after.
SCREEN = pygame.display.set_mode((1280, 720))
pygame.display.set_caption("Menu")

#Changes the background that is black to whatever we select.
BG = pygame.image.load("Background.png")

#Changes the font.
def get_font(size): # Returns Press-Start-2P in the desired size
    return pygame.font.Font("font.ttf", size)
    
    
#The actual action of runing the screen.
def play():
    while True:
        PLAY_MOUSE_POS = pygame.mouse.get_pos()

        SCREEN.fill("black")

        PLAY_TEXT = get_font(45).render("Choose your level:", True, "White")
        PLAY_RECT = PLAY_TEXT.get_rect(center=(640, 160))
        SCREEN.blit(PLAY_TEXT, PLAY_RECT)

        PLAY_BACK = Button(image=None, pos=(640, 600), 
                            text_input="BACK", font=get_font(75), base_color="White", hovering_color="Green")

        PLAY_BACK.changeColor(PLAY_MOUSE_POS)
        PLAY_BACK.update(SCREEN)
        
        
        #button level 1
        LVL_1 = Button(image = None, pos=(250,300),
						text_input="Lvl 1", font=get_font(40), base_color="White", hovering_color="Yellow")
        LVL_1.changeColor(PLAY_MOUSE_POS)
        LVL_1.update(SCREEN)
        
        #button level 2
        LVL_2 = Button(image = None, pos=(600,350),
						text_input="Lvl 2", font=get_font(40), base_color="White", hovering_color="Yellow")
        LVL_2.changeColor(PLAY_MOUSE_POS)
        LVL_2.update(SCREEN)
        
        #button level 3
        LVL_3 = Button(image = None, pos=(950,300),
						text_input="Lvl 3", font=get_font(40), base_color="White", hovering_color="Yellow")
        LVL_3.changeColor(PLAY_MOUSE_POS)
        LVL_3.update(SCREEN)


        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if PLAY_BACK.checkForInput(PLAY_MOUSE_POS):
                    main_menu()
                if LVL_1.checkForInput(PLAY_MOUSE_POS):
                    theMazeGame_lvl1()
                if LVL_2.checkForInput(PLAY_MOUSE_POS):
                    theMazeGame_lvl2()
                if LVL_3.checkForInput(PLAY_MOUSE_POS):
                    theMazeGame_lvl3()    
        pygame.display.update()
    


#opens the main menu of the game
def main_menu():
    while True:
        SCREEN.blit(BG, (0, 0))

        MENU_MOUSE_POS = pygame.mouse.get_pos()
        #set the font of the menu
        MENU_TEXT = get_font(100).render("MAIN MENU", True, "#b68f40")
        MENU_RECT = MENU_TEXT.get_rect(center=(640, 100))

        #set button settings
        PLAY_BUTTON = Button(image=pygame.image.load("Play Rect.png"), pos=(640, 250), 
                            text_input="PLAY", font=get_font(75), base_color="#d7fcd4", hovering_color="White")
        QUIT_BUTTON = Button(image=pygame.image.load("Quit Rect.png"), pos=(640, 550), 
                            text_input="QUIT", font=get_font(75), base_color="#d7fcd4", hovering_color="White")

        SCREEN.blit(MENU_TEXT, MENU_RECT)

        for button in [PLAY_BUTTON, QUIT_BUTTON]:
            button.changeColor(MENU_MOUSE_POS)
            button.update(SCREEN)
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if PLAY_BUTTON.checkForInput(MENU_MOUSE_POS):
                    play()
                if QUIT_BUTTON.checkForInput(MENU_MOUSE_POS):
                    pygame.quit()
                    sys.exit()


        pygame.display.update()
      
main_menu()

