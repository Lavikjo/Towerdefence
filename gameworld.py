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
		self.route = []


	def add_tower(self, tower, pos):
		if tower.set_world(self, pos):
			self.towers.append(tower)
			return self.squares[pos[0]][pos[1]].set_tower(tower):
		else:
			return False

	def add_enemy(self, enemy, pos):
		if enemy.set_world(self, pos):
			self.enemies.append(enemies)
			return self.squares[pos[0]][pos[1]].set_enemy(enemy):
		else:
			return False

	def remove_dead_enemies(self):
		'''
		Remove enemies flagged as dead from the game
		Returns amount of removed enemies
		'''
		count = 0
		for enemy in enemies:
			if not enemy.is_alive():
				self.enemies.remove(enemy)
				count += 1
		return count

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
		pass

	def get_route(self):
		'''
		Returns the route for the current map
		'''
		return self.route