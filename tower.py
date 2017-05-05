from unit import Unit
from enum import Enum
from random import Random, choice
from square import SquareType

class TowerType(Enum):
	ELECTRIC_TOWER = 0
	LASER_TOWER = 1

class Tower(Unit):

	

	
	def __init__(self, tower_type, configs):
		
		super().__init__(tower_type, configs)
		
		self.damage = int(self.configs[tower_type.name]['Damage'])
		self.range = int(self.configs[tower_type.name]['Range']) # range in squares to all cardinal directions
		self.attack_speed = float(self.configs[tower_type.name]['Attack_Speed']) # number of attack per second
		self.cost = int(self.configs[tower_type.name]['Cost'])
		self.upgrade_levels = {'UPGRADE_DMG': 1, 'UPGRADE_RANGE': 1, 'UPGRADE_SPEED': 1}
		self.upgrades = self.configs[tower_type.name]['Upgrades']

		self.target = None

		self.attack_cooldown = 0
		
	def set_ready(self):
		'''
		Sets tower attack-status to ready
		'''
		self.attack_ready = True
	
	def coords_in_range(self):
		'''
		Finds all the coordinates in range of tower
		'''
		possible_coords = []
		world = self.get_world()
		minx = max(0, self.pos[0] - self.range)
		miny = max(0, self.pos[1] - self.range)
		maxx = min(world.get_width() - 1, self.pos[0] + self.range) + 1
		maxy = min(world.get_height() - 1, self.pos[1] + self.range) + 1

		for x in range(minx, maxx):
			for y in range(miny, maxy):
				possible_coords.append((x, y))
		return possible_coords

	def coords_in_route(self, route):
		'''
		Filter only route squares from squares in range
		'''
		valid_types = [SquareType.START_SQUARE, SquareType.ROUTE_SQUARE, SquareType.END_SQUARE]
		route_coords = []

		for coord in self.coords_in_range():
			if self.get_world().get_square(coord).square_type in valid_types:
				route_coords.append(coord)
		return route_coords

	def find_enemies(self, coords):
		'''
		Find enemies that are in squares which are in range of tower
		'''
		found_enemies = []
		world = self.get_world()

		for coord in coords:
			found_enemies.extend(world.get_square(coord).get_enemies())
		return found_enemies

	def update(self, dt):
		# no cooldown, spawn enemy
		if self.attack_cooldown <= 0:
			if self.attack():
				self.attack_cooldown += 1/self.attack_speed
				return True

		# cooldown not expired, decrease it by logic timestep
		elif self.attack_cooldown > 0:
			self.attack_cooldown -= dt/1000
			return False
	def attack(self):
		'''
		Checks if tower can attack and deals damage to random enemy
		After attacking starts the cooldown timer
		'''	
		route = self.get_world().get_route()
		found_enemies = self.find_enemies(self.coords_in_route(route))
		if bool(found_enemies):
			random = Random(300)
			chosen_enemy = random.choice(found_enemies)
			chosen_enemy.damage(self.damage)
			self.target = chosen_enemy
			return True
		else:
			return False
	def can_afford(self, cost):
		if self.get_world().money - cost >= 0:
			self.get_world().money -= cost
			return True
		else:
			return False


	def upgrade(self, upgrade_type):
		'''
		Upgrade tower with correct upgrade if there is enough money
		'''
		upgrade_level = self.upgrade_levels[upgrade_type]
		max_level = self.upgrades['MAX_UPGRADE']
		money = self.get_world().money
		if upgrade_level != max_level:
			if(upgrade_type == 'UPGRADE_DMG'):
				cost = self.upgrades[(upgrade_type, upgrade_level)][1]
				if self.can_afford(cost):
					self.damage += self.upgrades[(upgrade_type, upgrade_level)][0]
					self.upgrade_levels[upgrade_type] += 1
			elif(upgrade_type == 'UPGRADE_RANGE'):
				cost = self.upgrades[(upgrade_type, upgrade_level)][1]
				if self.can_afford(cost):
					self.range += self.upgrades[(upgrade_type, upgrade_level)][0]
					self.upgrade_levels[upgrade_type] += 1
			elif(upgrade_type == 'UPGRADE_SPEED'):
				cost = self.upgrades[(upgrade_type, upgrade_level)][1]
				if self.can_afford(cost):
					self.attack_speed += self.upgrades[(upgrade_type, upgrade_level)][0]
					self.upgrade_levels[upgrade_type] += 1
			