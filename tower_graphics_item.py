from PyQt5 import QtWidgets, QtGui, QtCore

class TowerGraphicsItem(QtWidgets.QGraphicsPixmapItem):

	def __init__(self, tower, square_size):
		super().__init__()

		self.tower = tower
		self.square_size = square_size

		self.set_graphics()
		self.update()


	def set_graphics(self):
		offset = int(self.tower.configs[self.tower.type.name]['Graphic_Offset'])
		original = QtGui.QPixmap("textures/tilemap.png")
		
		rect = QtCore.QRect(64*offset, 64*offset, 64*(offset+1), 64*(offset+1))
		tile = QtGui.QPixmap()
		tile = original.copy(rect).scaled(self.square_size, self.square_size)

		self.setPixmap(tile)
	
	def update(self):
		pos = self.tower.get_pos()
		self.setPos(pos[0]*self.square_size, pos[1]*self.square_size)

