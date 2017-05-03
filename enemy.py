from enum import Enum
from square import Square, SquareType
from unit import Unit


class EnemyType(Enum):
	LIGHT_ENEMY = 0
	HEAVY_ENEMY = 1
	FAST_ENEMY = 2

class Enemy(Unit):

	def __init__(self, enemy_type):
		
		super().__init__(enemy_type)
		self.speed = 1
		self.prize = 0
		self.alive = True
		self.hp = 2
		self.route_number = 0

	def is_alive(self):

		return self.alive

	def move(self):
		'''
		Moves to next square in the predefined route
		'''
		route = self.get_world().get_route()
		current_square = self.get_current_square()

		if self.route_number == len(route) - 1:
			current_square.remove_unit(self)
			self.alive = False
			self.get_world().damage_base(1)
			return

		target_square = self.get_world().get_square(route[self.route_number+1])

		current_square.remove_unit(self)
		self.set_pos(route[self.route_number+1])
		target_square.set_enemy(self)

		self.route_number += 1

	def damage(self, amount):

		if self.hp > 0:
			'''
			Check if the damage kills the enemy and return True
			'''
			if (self.hp - amount) <= 0:
				self.hp = 0
				self.alive = False
				return True
			else:
				self.hp -= amount
				return False

	def is_at_goal(self):
		'''
		Checks if the current square enemy is standing on is the end goal
		'''
		current_square = self.get_world().get_square(self.get_pos())
		return current_square is SquareType.END_SQUARE