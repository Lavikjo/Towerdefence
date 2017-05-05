from square import Square
from spawner import Spawner

class GameWorld():

	def __init__(self, width, height, mapdata):

		self.squares = [None] * width

		for x in range(width):
			self.squares[x] = [None] * height
			for y in range(height):
				self.squares[x][y] = Square(mapdata[x][y])
		
		self.enemies = []
		self.towers = []
		self.wave_spawner = None

		self.base_hp = 10
		self.money = 100

		self.waves = []
		self.current_wave = 0
		self.max_waves = None
		self.total_enemies = 0
		
		self.route = []
		self.start_square_pos = None

		self.configs = {}

		self.alive = True

	def add_tower(self, tower, pos):
		'''
		Adds tower to gameworld if there is enough money
		'''
		if (self.money - tower.cost) >= 0 and tower.set_world(self, pos) and self.squares[pos[0]][pos[1]].set_tower(tower):
			self.money -= tower.cost
			self.towers.append(tower)
			return True
		else:
			return False

	def add_enemy(self, enemy, pos):
		'''
		Adds enemy to gameworld
		'''
		if enemy.set_world(self, pos) and self.squares[pos[0]][pos[1]].set_enemy(enemy):
			self.enemies.append(enemy)
			return True
		else:
			return False

	def remove_dead_enemies(self):
		'''
		Remove enemies flagged as dead from the game
		Returns amount of removed enemies
		'''
		count = 0
		for enemy in self.enemies:
			if not enemy.is_alive():
				pos = enemy.get_pos()
				self.squares[pos[0]][pos[1]].remove_unit(enemy)
				self.enemies.remove(enemy)
				count += 1
		return count

	def get_wave_total(self):
		'''
		Gets total amount of enemies in current wave
		'''
		return self.total_enemies
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

	def set_waves(self, waves):
		'''
		Sets wave data for the world
		'''
		self.waves = waves
		self.max_waves = len(waves)

	def next_wave(self):
		'''
		Starts new wave by creating a spawner
		'''
		if not self.get_number_of_enemies() and self.wave_spawner is None and self.current_wave is not len(self.waves):
			self.wave_spawner = Spawner(self, self.waves[self.current_wave], 1, 100)
			self.total_enemies = sum(self.waves[self.current_wave].values())
			self.current_wave += 1


	def set_route(self, route_data):
		'''
		Sets route data to world as possible coordinates
		'''
		self.route = route_data

	def get_route(self):
		'''
		Returns the route for the current map
		'''
		return self.route

	def get_width(self):
		
		return len(self.squares)

	def get_height(self):

		return len(self.squares[0])

	def get_towers(self):
		return self.towers

	def get_enemies(self):
		return self.enemies

	def get_square(self, pos):
		if 0 <= pos[0] < self.get_width() and 0 <= pos[1] < self.get_height():
			return self.squares[pos[0]][pos[1]]
		else:
			return Square(True)

	def get_start_square(self):
		'''
		Returns start square if it's set, otherwise finds and sets it
		'''
		if self.start_square_pos:
			return self.start_square_pos
		else:
			for y in range(self.get_height()):
				for x in range(self.get_width()):
					if self.squares[x][y].is_start():
						self.start_square_pos = (x, y)
						return self.start_square_pos

	def add_config(self, configs):
		'''
		Add configuration dictionary
		'''
		self.configs = configs

	def game_over(self):
		self.alive = False

	def __str__(self):
		'''
		Prints gameworld grid to console in readable format
		'''
		return_string = ""
		for y in range(self.get_height()):
			for x in range(self.get_width()):
				if self.squares[x][y].get_enemies():
					return_string += 'x'
				elif self.squares[x][y].get_tower():
					return_string += 'T'
				else:
					return_string += str(self.squares[x][y].square_type.value)
			return_string += '\n'
		return return_string