import pyxel

#pyxel edit "/Users/macbook/goldenpotato/python/Breakout/v1.0/my_resource.pyxres"

pyxel.init(100, 80, title = "Breakout")
pyxel.load("/Users/macbook/goldenpotato/python/Breakout/v1.0/my_resource.pyxres")

def update():
	if pyxel.btnp(pyxel.KEY_Q):
		pyxel.quit()
		
def draw():
	pyxel.cls(1)

pyxel.run(update, draw)