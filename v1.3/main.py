import pyxel

game_start_frame = 0
game_state = "TITLE"
version = "v1.3"

#pyxel edit "/Users/macbook/goldenpotato/python/Breakout/v1.2/my_resource.pyxres"

pyxel.init(160, 120, title = "Breakout")
pyxel.load("/Users/macbook/goldenpotato/python/Breakout/v1.2/my_resource.pyxres")

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
		self.x_speed = speed
		self.y_speed = -speed

	def update_ball(self):
		is_bound_x, is_bound_y = False, False
		for b in blocks:
			if(check_box_xline(b.x, b.y + b.height, b.width, self.x, self.y, self.size, self.size) and self.y_speed < 0):is_bound_y = True
			if(check_box_xline(b.x, b.y, b.width, self.x, self.y, self.size, self.size) and self.y_speed > 0):is_bound_y = True
			if(check_box_yline(b.x, b.y, b.height, self.x, self.y, self.size, self.size) and self.x_speed > 0):is_bound_x = True
			if(check_box_yline(b.x + b.width, b.y, b.height, self.x, self.y, self.size, self.size) and self.x_speed < 0):is_bound_x = True
		if(self.x <= 0 or self.x >= pyxel.width - self.size):self.x_speed *= -1
		if(self.y <= 0):self.y_speed *= -1
		if(is_bound_x):self.x_speed *= -1
		if(is_bound_y):self.y_speed *= -1
		if(check_box_xline(paddle.x, paddle.y, paddle.width, self.x, self.y, self.size, self.size)):self.y_speed *= -1
		self.x += self.x_speed
		self.y += self.y_speed

	def draw_ball(self):
		pyxel.rect(self.x, self.y, self.size, self.size, 10)

	def set_to_center(self, y):
		self.y = y
		self.x = (pyxel.width / 2) - (self.size / 2)
ball = Ball(0, 0, 4, 2)

class Block:
	def __init__(self, x, y, width, height, col):
		self.x = x
		self.y = y
		self.width = width
		self.height = height
		self.col = col

	def update_block(self):
		pass

	def draw_block(self):
		pyxel.rect(self.x, self.y, self.width, self.height, self.col)
		pyxel.rectb(self.x, self.y, self.width, self.height, 5)
block_width = 20
block_height = 10
block_col = 12
block_width_number = int(pyxel.width / block_width)
block_height_number = 6
blocks = []
remove_blocks = []
for i in range(block_height_number):
	for j in range(block_width_number):
		blocks.append(Block(block_width * j, block_height * i, block_width, block_height, block_col))

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
	if(pyxel.frame_count - game_start_frame > 30):
		paddle.update_paddle()
		ball.update_ball()
	for b in remove_blocks:
		blocks.remove(b)
		remove_blocks.remove(b)
	for b in blocks:
		if(check_box(b.x, b.y, b.width, b.height, ball.x, ball.y, ball.size, ball.size)):remove_blocks.append(b)

def draw_title_state():
	pyxel.cls(1)
	pyxel.mouse(True)
	pyxel.text(30, 30, "Breakout", 10)
	pyxel.text(30, 60, "Press [Space] to start", 7)
	pyxel.text(30, 80, "Press [Esc] to quit", 13)

def draw_play_state():
	pyxel.cls(1)
	pyxel.mouse(False)
	if(pyxel.frame_count - game_start_frame < 240):
		draw_countdown(pyxel.frame_count - game_start_frame)
	paddle.draw_paddle()
	ball.draw_ball()
	for b in blocks:
		b.draw_block()

def draw_countdown(t):
	if(t < 60):pyxel.text(78, 60, "3", 11)
	elif(t < 120):pyxel.text(78, 60, "2", 10)
	elif(t < 180):pyxel.text(78, 60, "1", 9)
	else:pyxel.text(76, 60, "Go!", 8)

def check_box(x1, y1, w1, h1, x2, y2, w2, h2):
	if(x1 + w1 < x2 or x2 + w2 < x1): return False
	if(y1 + h1 < y2 or y2 + h2 < y1): return False
	return True

def check_box_xline(x1, y1, w1, x2, y2, w2, h2):
	return y2 <= y1 <= y2 + h2 and(x2 <= x1 <= x2 + w2 or x1 + w1 >= x2 >= x1)

def check_box_yline(x1, y1, h1, x2, y2, w2, h2):
	return (y2 <= y1 <= y2 + h2 or y1 + h1 >= y2 >= y1)and x2 <= x1 <= x2 + w2

pyxel.run(update, draw)