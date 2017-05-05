from PyQt5 import QtWidgets, QtGui, QtCore
from unitgraphicsitem import UnitGraphicsItem

class EnemyGraphicsItem(UnitGraphicsItem):

	def __init__(self, enemy, square_size):
		super().__init__(enemy, square_size)

		self.enemy = enemy
		
		self.update()

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