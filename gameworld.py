from square import Square
from spawner import Spawner

class GameWorld():

	def __init__(self, width, height, mapdata):
		'''
		'''
		self.squares = [None] * width

		for x in range(width):
			self.squares[x] = [None] * height
			for y in range(height):
				self.squares[x][y] = Square(mapdata[x][y])
		self.enemies = []
		self.towers = []
		self.waves = None
		self.base_hp = 10
		self.money = 100
		self.current_wave = 0


	def add_tower(self, tower, pos, tower_type):
		pass

	def add_enemy(self, enemy, pos, enemy_type):
		pass

	def remove_dead_enemies(self):
		'''
		Removes enemies which are dead, returns number of enemies removed
		'''
		pass

	def get_number_of_enemies(self):
		'''
		Return numbers of alive enemies
		'''
		return len(self.enemies)

	def damage_base(self, amount):
		'''
		Damages player base, return True if player died
		'''
		if self.base_hp > 0:
			if (self.base_hp - amount) <= 0:
				self.base_hp = 0
				return True
			else:
				self.base_hp -= amount
				return False

	def next_wave(self):
		'''
		Starts new wave by creating a spawner
		'''
