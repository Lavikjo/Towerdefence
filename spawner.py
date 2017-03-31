from threading import Timer
from random import Random, choice

class Spawner():


	def __init__(self, world, wave, spawn_delay, seed):
		self.world = world
		self.wave = wave
		self.complete = False
		self.random = random.Random(seed)
		self.spawntimer = Timer(spawn_delay, self.spawn_enemy())
		self.spawntimer.start()

	def next_enemy(self):
		'''
		Returns next random enemy from wave
		'''
		# generate wave dictionary with only positive amounts
		wave = {key: value for (key, value) in self.wave.items() if value}

		if wave:
			enemy_type, amount = self.random.choice(list(self.wave.keys()))
		else:
			# no more enemies left so wave is complete
			self.complete = True

	def spawn_enemy(self):
		'''
		Spawns next random enemy to start square and starts spawntimer until wave is complete
		'''
		enemy_type = self.next_enemy()

		if not self.complete:
			self.wave[enemy_type] -= 1
			enemy = Enemy(enemy_type)
			self.world.add_enemy(enemy, self.world.get_start_square())
			self.spawntimer.start()
	
	def __str__(self):
		'''
		Prints types and amounts of enemies left on current wave
		'''
		for key, value in self.wave.items():
			print("Type: {}: {}".format(key, value))