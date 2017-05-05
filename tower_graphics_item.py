from PyQt5 import QtWidgets, QtGui, QtCore
from unitgraphicsitem import UnitGraphicsItem

class TowerGraphicsItem(UnitGraphicsItem):

	def __init__(self, tower, square_size):
		super().__init__(tower, square_size)

		self.tower = tower
		
		self.update()
	
	def update(self):
		pos = self.tower.get_pos()
		self.setPos(pos[0]*self.square_size, pos[1]*self.square_size)

