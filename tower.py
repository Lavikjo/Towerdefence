from unit import Unit
from enum import Enum
from threading import Timer

class TowerType(Enum):
	BASIC_TOWER = 0
	STRONG_TOWER = 1

class Tower(Unit):

	#self.upgrade_levels = {UPGRADE_DMG: 1, UPGRADE_RANGE: 1, UPGRADE_SPEED: 1}
	#self.upgrades = {(UPGRADE_DMG, 1): 15}

	
	def __init__(self, tower_type):
		
		super().__init__(tower_type)
		self.damage = 1
		self.range = 3 # range in squares to all cardinal directions
		self.attack_speed = 1 # number of attack per second

		self.attack_ready = True
		self.cooldown_timer = None

	def set_ready(self):
		'''
		Sets tower attack-status to ready
		'''
		self.attack_ready = True

	def is_in_range(self, enemy):
		#print((self.pos[0] - enemy.pos[0])**2 + (self.pos[1] - enemy.pos[1])**2)
		return self.range**2 >= ((self.pos[0] - enemy.pos[0])**2 + (self.pos[1] - enemy.pos[1])**2)

	def can_attack(self, enemy):
		'''
		Returns True if enemy is in range of tower and tower hasn't attacked recently
		'''
		return enemy.hp > 0 and self.attack_ready and self.is_in_range(enemy)


	def attack(self, enemy):
		'''
		Checks if tower can attack and deals damage to enemy
		After attacking starts the cooldown timer
		'''
		if self.can_attack(enemy):
			enemy.damage(self.damage)
			self.attack_ready = False
			self.cooldown_timer = Timer(1/self.attack_speed, self.set_ready())

	def upgrade(self, upgrade_type):
		upgrade_level = self.upgrade_levels[upgrade_type]

		if(upgrade_type == UPGRADE_DMG):
			self.damage += self.upgrades[(upgrade_type, upgrade_level)]
		elif(upgrade_type == UPGRADE_RANGE):
			self.range += self.upgrades[(upgrade_type, upgrade_level)]
		elif(upgrade_type == UPGRADE_SPEED):
			self.attack_speed += self.upgrades[(upgrade_type, upgrade_level)]