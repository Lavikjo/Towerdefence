from PyQt5 import QtWidgets, QtGui, QtCore

class EnemyGraphicsItem(QtWidgets.QGraphicsPixmapItem):

	def __init__(self, enemy, square_size):
		super().__init__()

		self.enemy = enemy
		self.square_size = square_size

		self.set_graphics()
		self.update()


	def set_graphics(self):
		'''
		Crops and scales correct tile from tilemap and sets it as current graphic
		'''
		offset_x = int(self.enemy.configs[self.enemy.type.name]['Graphic_Offset_X'])
		offset_y = int(self.enemy.configs[self.enemy.type.name]['Graphic_Offset_Y'])
		original = QtGui.QPixmap("textures/tilemap.png")
		
		rect = QtCore.QRect(64*offset_x, 64*offset_y, 64, 64)
		tile = QtGui.QPixmap()
		tile = original.copy(rect).scaled(self.square_size, self.square_size)

		tile.setMask(tile.createHeuristicMask())
		self.setPixmap(tile)

	def interpolate(self, start, end, t):
		return ((1 - t)*start[0] + t*end[0], (1 - t)*start[1] + t*end[1])

	def update(self):
		'''
		Linearly interpolates enemy movement so it looks smooth
		'''
		world = self.enemy.get_world()
		current_pos = self.enemy.get_pos()
		try:
			next_pos = world.get_route()[self.enemy.route_number + 1]

			t = self.enemy.move_threshold

			graphic_pos = self.interpolate(current_pos, next_pos, t)
			self.setPos(graphic_pos[0]*self.square_size, graphic_pos[1]*self.square_size)
		except IndexError:
			# Handles corner case with graphical item reaching the end before logic removes dead enemy
			return