from PyQt5 import QtWidgets, QtGui, QtCore

class UnitGraphicsItem(QtWidgets.QGraphicsPixmapItem):

	def __init__(self, unit, square_size):
		super().__init__()

		self.unit = unit
		self.square_size = square_size

		self.set_graphics()


	def set_graphics(self):
		'''
		Crops and scales correct tile from tilemap and sets it as current graphic
		'''
		offset_x = int(self.unit.configs[self.unit.type.name]['Graphic_Offset_X'])
		offset_y = int(self.unit.configs[self.unit.type.name]['Graphic_Offset_Y'])
		original = QtGui.QPixmap("textures/tilemap.png")
		
		rect = QtCore.QRect(64*offset_x, 64*offset_y, 64, 64)
		tile = QtGui.QPixmap()
		tile = original.copy(rect).scaled(self.square_size, self.square_size)

		tile.setMask(tile.createHeuristicMask())
		self.setPixmap(tile)
