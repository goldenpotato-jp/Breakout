import pyxel

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
	global game_state
	if(pyxel.btn(pyxel.KEY_SPACE)):game_state = "PLAY"

def update_play_state():
	pass

def draw_title_state():
	pyxel.cls(1)
	pyxel.mouse(True)
	pyxel.text(30, 30, "Breakout", 10)
	pyxel.text(30, 60, "Press [Space] to start", 7)
	pyxel.text(30, 80, "Press [Esc] to quit", 13)

def draw_play_state():
	pass

pyxel.run(update, draw)