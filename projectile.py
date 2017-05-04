from PyQt5 import QtWidgets, QtGui, QtCore
from enum import Enum
import math

class ProjectileType(Enum):
	LASER = 0
	ELECTRIC = 1

class Projectile(QtWidgets.QGraphicsPixmapItem):

	def __init__(self, enemy, tower, square_size):
		super().__init__()

		self.enemy = enemy
		self.tower = tower
		self.square_size = square_size
		self.alive = True

		self.type = ProjectileType[self.tower.configs[self.tower.type.name]['ProjectileType']]
		self.alive_time = 0.2
		self.move_threshold = 0
		self.speed = 0

		self.set_graphics()

	def is_alive(self):
		return self.alive

	def set_graphics(self):

		# draw laser beam to middle of moving enemy
		if self.type == ProjectileType.LASER:
			graphic = QtGui.QPixmap(900, 900)
			graphic.fill(QtGui.QColor(0))
			painter = QtGui.QPainter(graphic)
			painter.setPen(QtGui.QColor(255, 0, 0))

			start = self.tower.get_pos()
			enemy_pos = self.enemy.get_pos()
			threshold = self.enemy.move_threshold
			world = self.enemy.get_world()

			try:
				next_enemy_pos = world.get_route()[self.enemy.route_number + 1]
				graphic_pos = self.interpolate(enemy_pos, next_enemy_pos, threshold)

				painter.drawLine(start[0]*self.square_size + self.square_size/2, start[1]*self.square_size + self.square_size/2, graphic_pos[0]*self.square_size + self.square_size/2, graphic_pos[1]*self.square_size + self.square_size/2)
				painter.end()
				graphic.setMask(graphic.createHeuristicMask())
				self.setPixmap(graphic)
			except IndexError:
				# Handles corner case with graphical item reaching the end before logic removes dead enemy
				return

		# draw traditional projectile
		elif self.type == ProjectileType.ELECTRIC:
			offset_x = int(self.tower.configs[self.tower.type.name]['Projectile_Graphic_Offset_X'])
			offset_y = int(self.tower.configs[self.tower.type.name]['Projectile_Graphic_Offset_Y'])
			original = QtGui.QPixmap("textures/tilemap.png")
			
			rect = QtCore.QRect(64*offset_x, 64*offset_y, 64, 64)
			tile = QtGui.QPixmap()
			tile = original.copy(rect).scaled(self.square_size, self.square_size)

			tile.setMask(tile.createHeuristicMask())
			self.setPixmap(tile)

	def interpolate(self, start, end, t):
		return ((1 - t)*start[0] + t*end[0], (1 - t)*start[1] + t*end[1])

	def update(self, dt):
		
		if self.alive_time <= 0:
			self.alive = False
		else:

			if self.type == ProjectileType.ELECTRIC:
				enemy_pos = self.enemy.get_pos()
				tower_pos = self.tower.get_pos()
				threshold = self.enemy.move_threshold
				world = self.enemy.get_world()
				next_enemy_pos = world.get_route()[self.enemy.route_number + 1]
				enemy_real_pos = self.interpolate(enemy_pos, next_enemy_pos, threshold)

				# calculate speed of projectile based on distance to enemy and alive time
				# bullet will accelerate depending on the distance

				if not self.speed:
					self.speed = math.sqrt((enemy_real_pos[0] - tower_pos[0])**2 + (enemy_real_pos[1] - tower_pos[1])**2)/self.alive_time
				try:
					if self.move_threshold >= 1:
						self.alive = False
					elif self.move_threshold < 1:
						
						self.move_threshold += self.speed*dt/1000
						graphic_pos = self.interpolate(tower_pos, enemy_real_pos, self.move_threshold)
						self.setPos(graphic_pos[0]*self.square_size, graphic_pos[1]*self.square_size)
				except IndexError:
					# Handles corner case with graphical item reaching the end before logic removes dead enemy
					return


			self.alive_time -= dt/1000