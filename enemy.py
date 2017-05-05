from enum import Enum
from square import Square, SquareType
from unit import Unit


class EnemyType(Enum):
	LIGHT_ENEMY = 0
	HEAVY_ENEMY = 1
	FAST_ENEMY = 2

class Enemy(Unit):

	def __init__(self, enemy_type, configs):
		
		super().__init__(enemy_type, configs)
		self.speed = float(self.configs[enemy_type.name]['Speed'])
		self.prize = int(self.configs[enemy_type.name]['Prize'])
		self.hp = int(self.configs[enemy_type.name]['Health'])
		self.base_damage = int(self.configs[enemy_type.name]['Damage'])
		self.alive = True

		self.route_number = 0
		self.move_threshold = 0

	def is_alive(self):

		return self.alive

	def update(self, dt):
		# threshold reached, move to next square
		if self.move_threshold >= 1:
			self.move()
			self.move_threshold = 0
		# threshold not reached, increase by logic timestep multiplied with speed
		elif self.move_threshold < 1:
			self.move_threshold += self.speed*dt/1000
	
	def move(self):
		'''
		Moves to next square in the predefined route
		'''
		route = self.get_world().get_route()
		current_square = self.get_current_square()

		# check if end square has been reached
		if self.route_number == len(route) - 1:
			current_square.remove_unit(self)
			self.alive = False

			# sets game over if enemy kills player
			if self.get_world().damage_base(self.base_damage):
				self.get_world().game_over()
			return

		target_square = self.get_world().get_square(route[self.route_number+1])

		current_square.remove_unit(self)
		self.set_pos(route[self.route_number+1])
		target_square.set_enemy(self)

		self.route_number += 1

	def damage(self, amount):
		'''
		Check if the damage kills the enemy and return True
		'''
		if self.hp > 0:
			
			if (self.hp - amount) <= 0:
				self.hp = 0
				self.world.money += self.prize
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