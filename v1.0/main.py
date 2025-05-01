import pyxel

game_start_frame = 0
game_state = "TITLE"

#pyxel edit "/Users/macbook/goldenpotato/python/Breakout/v1.0/my_resource.pyxres"

pyxel.init(160, 120, title = "Breakout")
pyxel.load("/Users/macbook/goldenpotato/python/Breakout/v1.0/my_resource.pyxres")

def update():
	if(game_state == "TITLE"):update_title_state()
	elif(game_state == "PLAY"):update_play_state()

def draw():
	pyxel.cls(0)
	if(game_state == "TITLE"):draw_title_state()
	elif(game_state == "PLAY"):draw_play_state()

def update_title_state():
	global game_start_frame, game_state
	if(pyxel.btn(pyxel.KEY_SPACE)):
		game_state = "PLAY"
		game_start_frame = pyxel.frame_count

def update_play_state():
	pass

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

def draw_countdown(t):
	if(t < 60):pyxel.text(78, 60, "3", 11)
	elif(t < 120):pyxel.text(78, 60, "2", 10)
	elif(t < 180):pyxel.text(78, 60, "1", 9)
	else:pyxel.text(76, 60, "Go!", 8)

pyxel.run(update, draw)