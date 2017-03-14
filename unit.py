class Unit():

	def __init__(self):
		self.pos = None
		self.world = None

	def get_pos(self):

		return self.pos

	def get_world(self):

		return self.world

	def set_world(self, world, pos):

		if not world.get_square(pos).is_empty() or self.get_world() is not None:
			return False
		else:
			self.world = world
			self.pos = pos
			return True 

