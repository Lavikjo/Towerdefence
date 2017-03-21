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

		self.base_hp = 10
		self.money = 100

		self.waves = []
		self.current_wave = 0
		self.max_waves = None
		
		self.route = []
		self.start_square = None

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
		if not self.get_number_of_enemies():
			self.current_wave += 1
			wave_spawner = Spawner(self, self.waves[self.current_wave], 0.3, 100)

	def get_route(self):
		'''
		Returns the route for the current map
		'''
		return self.route

	def get_width(self):
		
		return len(self.squares)

	def get_height(self):

		return len(self.squares[0])

	def get_start_square(self):
		'''
		Returns start square if it's set, otherwise finds and sets it
		'''
		if self.start_square:
			return self.start_square
		else:
			for x in range(self.get_width()):
				for y in range(self.get_height()):
					if self.squares[x][y].is_start():
						self.start_square = self.squares[x][y]
						return self.start_square