import pyxel

class Paddle:
	def __init__(self, x, y, width, height, speed):
		self.x = x
		self.y = y
		self.width = width
		self.height = height
		self.speed = speed

	def update_paddle(self):
		if(pyxel.btn(pyxel.KEY_A) or pyxel.btn(pyxel.KEY_LEFT)):self.x -= self.speed
		if(pyxel.btn(pyxel.KEY_D) or pyxel.btn(pyxel.KEY_RIGHT)):self.x += self.speed
		if(self.x < 0):self.x = 0
		elif(self.x > pyxel.width - self.width):self.x = pyxel.width - self.width


	def draw_paddle(self):
		pyxel.rect(self.x, self.y, self.width, self.height, 7)

	def set_to_center(self, y):
		self.y = y
		self.x = (pyxel.width / 2) - (self.width / 2)
paddle = Paddle(0, 0, 30, 5, 3)

class Ball:
	def __init__(self, x, y, size, speed):
		self.x = x
		self.y = y
		self.size = size
		self.speed = speed

	def update_ball(self):
		pass

	def draw_ball(self):
		pyxel.rect(self.x, self.y, self.size, self.size, 10)

	def set_to_center(self, y):
		self.y = y
		self.x = (pyxel.width / 2) - (self.size / 2)
ball = Ball(0, 0, 4, 3)

game_start_frame = 0
game_state = "TITLE"
version = "v1.2"

#pyxel edit "/Users/macbook/goldenpotato/python/Breakout/v1.1/my_resource.pyxres"

pyxel.init(160, 120, title = "Breakout")
pyxel.load("/Users/macbook/goldenpotato/python/Breakout/v1.1/my_resource.pyxres")

def update():
	if(game_state == "TITLE"):update_title_state()
	elif(game_state == "PLAY"):update_play_state()

def draw():
	pyxel.cls(0)
	if(game_state == "TITLE"):draw_title_state()
	elif(game_state == "PLAY"):draw_play_state()
	pyxel.text(140, 110, version, 13)

def update_title_state():
	global game_start_frame, game_state
	if(pyxel.btn(pyxel.KEY_SPACE)):
		game_state = "PLAY"
		game_start_frame = pyxel.frame_count
		paddle.set_to_center(100)
		ball.set_to_center(90)

def update_play_state():
	if(pyxel.frame_count - game_start_frame > 240):
		paddle.update_paddle()

def draw_title_state():
	pyxel.cls(1)
	pyxel.mouse(True)
	pyxel.text(30, 30, "Breakout", 10)
	pyxel.text(30, 60, "Press [Space] to start", 7)
	pyxel.text(30, 80, "Press [Esc] to quit", 13)

def draw_play_state():
	pyxel.cls(1)
	if(pyxel.frame_count - game_start_frame < 240):
		draw_countdown(pyxel.frame_count - game_start_frame)
	paddle.draw_paddle()
	ball.draw_ball()

def draw_countdown(t):
	if(t < 60):pyxel.text(78, 60, "3", 11)
	elif(t < 120):pyxel.text(78, 60, "2", 10)
	elif(t < 180):pyxel.text(78, 60, "1", 9)
	else:pyxel.text(76, 60, "Go!", 8)

pyxel.run(update, draw)