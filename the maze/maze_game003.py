from maze_generator002 import *
from last_window import * 





#global values
def get_record():
	try:
		with open('record') as f:
			return f.readline()
	except FileNotFoundError:
		with open('record', 'w') as f:
			f.write('0')
			return 0
FPS = 60
time = 100
score = 10
record = get_record()



#there are 3 functions but with differnt levels. They are the same function just with different values, so no need to check each of those

def theMazeGame_lvl1():


	class Food:
		def __init__(self):
			self.img = pygame.image.load('banana.png').convert_alpha()
			self.img = pygame.transform.scale(self.img, (TILE(1) - 10, TILE(1) - 10))
			self.rect = self.img.get_rect()
			self.set_pos()

		def set_pos(self):
			self.rect.bottomright = TILE(1) + 907, TILE(1) + 620

		def draw(self):
			game_surface.blit(self.img, self.rect)


	def is_collide(x, y):
		tmp_rect = player_rect.move(x, y)
		if tmp_rect.collidelist(walls_collide_list) == -1:
			return False
		return True


	#a player reaches the cherry
	def eat_food():
		for food in food_list:
			if player_rect.collidepoint(food.rect.center):
				food.set_pos()
				return True
		return False


	def is_game_over():
		global time, score, record, FPS
		#stops when reaches the cherry or time ends
		if time < 0 or eat_food():
			pygame.time.wait(2)
			set_record(record, score)
			record = get_record()
			last_window()


	def get_record():
		try:
			with open('record') as f:
				return f.readline()
		except FileNotFoundError:
			with open('record', 'w') as f:
				f.write('0')
				return 0


	def set_record(record, score):
		rec = max(int(record), score)
		with open('record', 'w') as f:
			f.write(str(rec))



	FPS = 60

	pygame.init()
	game_surface = pygame.Surface(RES)
	surface = pygame.display.set_mode((WIDTH + 300, HEIGHT))
	clock = pygame.time.Clock()

	# images
	bg_game = pygame.image.load('Background.png').convert()
	bg = pygame.image.load('bg_main.png').convert()

	# get maze
	maze = lev1MAZEgen()

	# player settings
	player_speed = 5
	player_img = pygame.image.load('THEmonkey.png').convert_alpha()
	player_img = pygame.transform.scale(player_img, (TILE(1) - 2 * maze[0].thickness, TILE(1) - 2 * maze[0].thickness))
	player_rect = player_img.get_rect()
	player_rect.center = TILE(1) // 2, TILE(1) // 2
	directions = {'LEFT': (-player_speed, 0), 'RIGHT': (player_speed, 0), 'UP': (0, -player_speed), 'DOWN': (0, player_speed),'nothing':(0,0)}
	keys = {'LEFT': pygame.K_LEFT, 'RIGHT': pygame.K_RIGHT, 'UP': pygame.K_UP, 'DOWN': pygame.K_DOWN,'nothing':0}
	direction = (0, 0)

	# food settings
	food_list = [Food() for i in range(3)]

	# collision list
	walls_collide_list = sum([cell.get_rects() for cell in maze], [])

	# timer, score, record
	pygame.time.set_timer(pygame.USEREVENT, 1000)
	time = 100
#	score = 0
	record = get_record()

	# fonts
	font = pygame.font.Font("font.ttf", 40)
	text_font = pygame.font.Font("font.ttf", 40)

	def playGame():
		global time, score, record
		directions = {'LEFT': (-player_speed, 0), 'RIGHT': (player_speed, 0), 'UP': (0, -player_speed), 'DOWN': (0, player_speed),'nothing':(0,0)}
		keys = {'LEFT': pygame.K_LEFT, 'RIGHT': pygame.K_RIGHT, 'UP': pygame.K_UP, 'DOWN': pygame.K_DOWN,'nothing':0}
		direction = (0, 0)
		time = 100
		while True:

			surface.blit(bg, (WIDTH, 0))
			surface.blit(game_surface, (0, 0))
			game_surface.blit(bg_game, (0, 0))

			for event in pygame.event.get():
				if event.type == pygame.QUIT:
					exit()
				if event.type == pygame.USEREVENT:
					time -= 1
					 # controls and movement
			pressed_key = pygame.key.get_pressed()
				
			for key, key_value in keys.items():
				if pressed_key[key_value] and not is_collide(*directions[key]):
					direction = directions[key]
					break
				if not is_collide(*direction):
					player_rect.move_ip(direction)
					

			# draw maze
			[cell.draw(game_surface) for cell in maze]

			# gameplay
			if eat_food():
				is_game_over()
				
			if time==80:
				score-=0.01
			elif time==60:
				score-=0.05
			elif time==20:
				score-=0.09

			

			# draw player
			game_surface.blit(player_img, player_rect)

			# draw food
			[food.draw() for food in food_list]

			# draw stats
			surface.blit(text_font.render('TIME', True, pygame.Color('cyan'), True), (WIDTH + 35, 15))
			surface.blit(font.render(f'{time}', True, pygame.Color('cyan')), (WIDTH + 45, 90))
			surface.blit(text_font.render('score:', True, pygame.Color('forestgreen'), True), (WIDTH + 35, 255))
			surface.blit(font.render(f'{score}', True, pygame.Color('forestgreen')), (WIDTH + 50, 320))
			surface.blit(text_font.render('record:', True, pygame.Color('magenta'), True), (WIDTH + 35, 470))
			surface.blit(font.render(f'{record}', True, pygame.Color('magenta')), (WIDTH + 45, 550))

			# print(clock.get_fps())
			pygame.display.flip()
			clock.tick(FPS)

	playGame()














def theMazeGame_lvl2():


	class Food:
		def __init__(self):
			self.img = pygame.image.load('banana.png').convert_alpha()
			self.img = pygame.transform.scale(self.img, (TILE(2) - 10, TILE(2) - 10))
			self.rect = self.img.get_rect()
			self.set_pos()

		def set_pos(self):
			self.rect.bottomright = TILE(2) + 932, TILE(2) + 600

		def draw(self):
			game_surface.blit(self.img, self.rect)


	def is_collide(x, y):
		tmp_rect = player_rect.move(x, y)
		if tmp_rect.collidelist(walls_collide_list) == -1:
			return False
		return True


	#a player reaches the cherry
	def eat_food():
		for food in food_list:
			if player_rect.collidepoint(food.rect.center):
				food.set_pos()
				return True
		return False


	def is_game_over():
		global time, score, record, FPS
		#stops when reaches the cherry or time ends
		if time < 0 or eat_food():
			pygame.time.wait(0)
			set_record(record, score)
			record = get_record()
			last_window()


	def get_record():
		try:
			with open('record') as f:
				return f.readline()
		except FileNotFoundError:
			with open('record', 'w') as f:
				f.write('0')
				return 0


	def set_record(record, score):
		rec = max(int(record), score)
		with open('record', 'w') as f:
			f.write(str(rec))



	#FPS = 100

	pygame.init()
	game_surface = pygame.Surface(RES)
	surface = pygame.display.set_mode((WIDTH + 300, HEIGHT))
	clock = pygame.time.Clock()

	# images
	bg_game = pygame.image.load('Background.png').convert()
	bg = pygame.image.load('bg_main.png').convert()

	# get maze
	maze = lev2MAZEgen()

	# player settings
	player_speed = 5
	player_img = pygame.image.load('THEmonkey.png').convert_alpha()
	player_img = pygame.transform.scale(player_img, (TILE(2) - 2 * maze[0].thickness, TILE(2) - 2 * maze[0].thickness))
	player_rect = player_img.get_rect()
	player_rect.center = TILE(2) // 2, TILE(2) // 2
	directions = {'LEFT': (-player_speed, 0), 'RIGHT': (player_speed, 0), 'UP': (0, -player_speed), 'DOWN': (0, player_speed)}
	keys = {'LEFT': pygame.K_LEFT, 'RIGHT': pygame.K_RIGHT, 'UP': pygame.K_UP, 'DOWN': pygame.K_DOWN}
	direction = (0, 0)

	# food settings
	food_list = [Food() for i in range(3)]

	# collision list
	walls_collide_list = sum([cell.get_rects() for cell in maze], [])

	# timer, score, record
	pygame.time.set_timer(pygame.USEREVENT, 1000)
	time = 10
	score = 0
	record = 2
	record = get_record()

	# fonts
	font = pygame.font.Font("font.ttf", 40)
	text_font = pygame.font.Font("font.ttf", 40)

	def playGame():
		global time, score
		directions = {'LEFT': (-player_speed, 0), 'RIGHT': (player_speed, 0), 'UP': (0, -player_speed), 'DOWN': (0, player_speed)}
		keys = {'LEFT': pygame.K_LEFT, 'RIGHT': pygame.K_RIGHT, 'UP': pygame.K_UP, 'DOWN': pygame.K_DOWN}
		direction = (0, 0)
		#time = 10
		global time
		while True:

			surface.blit(bg, (WIDTH, 0))
			surface.blit(game_surface, (0, 0))
			game_surface.blit(bg_game, (0, 0))

			for event in pygame.event.get():
				if event.type == pygame.QUIT:
					exit()
				if event.type == pygame.USEREVENT:
					time -= 1
					 # controls and movement
			pressed_key = pygame.key.get_pressed()
				
			for key, key_value in keys.items():
				if pressed_key[key_value] and not is_collide(*directions[key]):
					direction = directions[key]
					break
				if not is_collide(*direction):
					player_rect.move_ip(direction)

			# draw maze
			[cell.draw(game_surface) for cell in maze]

			# gameplay
			if eat_food():
				is_game_over()
			if time<=0:
				is_game_over()
				
			
			if time==80:
				score-=0.01
			elif time==60:
				score-=0.05
			elif time==20:
				score-=0.09


			# draw player
			game_surface.blit(player_img, player_rect)

			# draw food
			[food.draw() for food in food_list]

			# draw stats
			surface.blit(text_font.render('TIME', True, pygame.Color('cyan'), True), (WIDTH + 35, 15))
			surface.blit(font.render(f'{time}', True, pygame.Color('cyan')), (WIDTH + 45, 90))
			surface.blit(text_font.render('score:', True, pygame.Color('forestgreen'), True), (WIDTH + 35, 255))
			surface.blit(font.render(f'{score}', True, pygame.Color('forestgreen')), (WIDTH + 50, 320))
			surface.blit(text_font.render('record:', True, pygame.Color('magenta'), True), (WIDTH + 35, 470))
			surface.blit(font.render(f'{record}', True, pygame.Color('magenta')), (WIDTH + 45, 550))

			# print(clock.get_fps())
			pygame.display.flip()
			clock.tick(FPS)
	
	return playGame()
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
def theMazeGame_lvl3():


	class Food:
		def __init__(self):
			self.img = pygame.image.load('banana.png').convert_alpha()
			self.img = pygame.transform.scale(self.img, (TILE(3) - 10, TILE(3) - 10))
			self.rect = self.img.get_rect()
			self.set_pos()

		def set_pos(self):
			self.rect.bottomright = TILE(3) + 940, TILE(3) + 660

		def draw(self):
			game_surface.blit(self.img, self.rect)


	def is_collide(x, y):
		tmp_rect = player_rect.move(x, y)
		if tmp_rect.collidelist(walls_collide_list) == -1:
			return False
		return True


	#a player reaches the cherry
	def eat_food():
		for food in food_list:
			if player_rect.collidepoint(food.rect.center):
				food.set_pos()
				return True
		return False


	def is_game_over():
		global time, score, record, FPS
		#stops when reaches the cherry or time ends
		if time < 0 or eat_food():
			pygame.time.wait(2)
			set_record(record, score)
			record = get_record()
			last_window()


	def get_record():
		try:
			with open('record') as f:
				return f.readline()
		except FileNotFoundError:
			with open('record', 'w') as f:
				f.write('0')
				return 0


	def set_record(record, score):
		rec = max(int(record), score)
		with open('record', 'w') as f:
			f.write(str(rec))



	#FPS = 75

	pygame.init()
	game_surface = pygame.Surface(RES)
	surface = pygame.display.set_mode((WIDTH + 300, HEIGHT))
	clock = pygame.time.Clock()

	# images
	bg_game = pygame.image.load('Background.png').convert()
	bg = pygame.image.load('bg_main.png').convert()

	# get maze
	maze = lev3MAZEgen()

	# player settings
	player_speed = 5
	player_img = pygame.image.load('THEmonkey.png').convert_alpha()
	player_img = pygame.transform.scale(player_img, (TILE(3) - 2 * maze[0].thickness, TILE(3) - 2 * maze[0].thickness))
	player_rect = player_img.get_rect()
	player_rect.center = TILE(3) // 2, TILE(3) // 2
	directions = {'LEFT': (-player_speed, 0), 'RIGHT': (player_speed, 0), 'UP': (0, -player_speed), 'DOWN': (0, player_speed)}
	keys = {'LEFT': pygame.K_LEFT, 'RIGHT': pygame.K_RIGHT, 'UP': pygame.K_UP, 'DOWN': pygame.K_DOWN}
	direction = (0, 0)

	# food settings
	food_list = [Food() for i in range(3)]

	# collision list
	walls_collide_list = sum([cell.get_rects() for cell in maze], [])

	# timer, score, record
	pygame.time.set_timer(pygame.USEREVENT, 1000)
	#time = 5
	#score = 0
	#record = get_record()

	# fonts
	font = pygame.font.Font("font.ttf", 40)
	text_font = pygame.font.Font("font.ttf", 40)

	def playGame():
		global time, score
		directions = {'LEFT': (-player_speed, 0), 'RIGHT': (player_speed, 0), 'UP': (0, -player_speed), 'DOWN': (0, player_speed)}
		keys = {'LEFT': pygame.K_LEFT, 'RIGHT': pygame.K_RIGHT, 'UP': pygame.K_UP, 'DOWN': pygame.K_DOWN}
		direction = (0, 0)
		#time = 5
		while True:

			surface.blit(bg, (WIDTH, 0))
			surface.blit(game_surface, (0, 0))
			game_surface.blit(bg_game, (0, 0))

			for event in pygame.event.get():
				if event.type == pygame.QUIT:
					exit()
				if event.type == pygame.USEREVENT:
					time -= 1
					 # controls and movement
			pressed_key = pygame.key.get_pressed()
				
			for key, key_value in keys.items():
				if pressed_key[key_value] and not is_collide(*directions[key]):
					direction = directions[key]
					break
				if not is_collide(*direction):
					player_rect.move_ip(direction)

			# draw maze
			[cell.draw(game_surface) for cell in maze]

			# gameplay
			if eat_food():
				is_game_over()
				
			if time<0:
				is_game_over()
				
			if time==80:
				score-=0.01
			elif time==60:
				score-=0.05
			elif time==20:
				score-=0.09


			# draw player
			game_surface.blit(player_img, player_rect)

			# draw food
			[food.draw() for food in food_list]

			# draw stats
			surface.blit(text_font.render('TIME', True, pygame.Color('cyan'), True), (WIDTH + 35, 15))
			surface.blit(font.render(f'{time}', True, pygame.Color('cyan')), (WIDTH + 45, 90))
			surface.blit(text_font.render('score:', True, pygame.Color('forestgreen'), True), (WIDTH + 35, 255))
			surface.blit(font.render(f'{score}', True, pygame.Color('forestgreen')), (WIDTH + 50, 320))
			surface.blit(text_font.render('record:', True, pygame.Color('magenta'), True), (WIDTH + 35, 470))
			surface.blit(font.render(f'{record}', True, pygame.Color('magenta')), (WIDTH + 45, 550))

			# print(clock.get_fps())
			pygame.display.flip()
			clock.tick(FPS)

	playGame()
