from random import Random, choice
from enemy import Enemy, EnemyType

class Spawner():


	def __init__(self, world, wave, spawn_delay, seed):
		self.world = world
		self.wave = wave
		self.complete = False
		self.random = Random(seed)
		self.spawn_delay = spawn_delay
		self.spawn_cooldown = 0

	def next_enemy(self):
		'''
		Returns next random enemy from wave
		'''
		# generate wave dictionary with only positive amounts
		wave = {key: value for (key, value) in self.wave.items() if value}
		if bool(wave):
			enemy_type = self.random.choice(list(wave.keys()))
			return enemy_type
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
			enemy = Enemy(EnemyType[enemy_type])
			self.world.add_enemy(enemy, self.world.get_start_square())	
			
	def update(self, dt):

		# no cooldown, spawn enemy
		if self.spawn_cooldown <= 0:
			self.spawn_enemy()
			self.spawn_cooldown += self.spawn_delay
		# cooldown not expired, decrease it by logic timestep
		elif self.spawn_cooldown > 0:
			self.spawn_cooldown -= dt/1000

	def __str__(self):
		'''
		Prints types and amounts of enemies left on current wave
		'''
		for key, value in self.wave.items():
			print("Type: {}: {}".format(key, value))