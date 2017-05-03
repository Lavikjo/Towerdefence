from PyQt5 import QtWidgets, QtGui, QtCore

class EnemyGraphicsItem(QtWidgets.QGraphicsPixmapItem):

	def __init__(self, enemy, square_size):
		super().__init__()

		self.enemy = enemy
		self.square_size = square_size

		self.set_graphics()
		self.update()


	def set_graphics(self):
		offset = 0
		original = QtGui.QPixmap("textures/tilemap.png")
		
		rect = QtCore.QRect(64*offset, 64*offset, 64*(offset+1), 64*(offset+1))
		tile = QtGui.QPixmap()
		tile = original.copy(rect).scaled(self.square_size, self.square_size)

		self.setPixmap(tile)

	def interpolate(self, start, end, t):
		return ((1 - t)*start[0] + t*end[0], (1 - t)*start[1] + t*end[1])

	def update(self):
		world = self.enemy.get_world()
		current_pos = self.enemy.get_pos()
		next_pos = world.get_route()[self.enemy.route_number + 1]
		t = self.enemy.move_threshold

		graphic_pos = self.interpolate(current_pos, next_pos, t)
		self.setPos(graphic_pos[0]*self.square_size, graphic_pos[1]*self.square_size)