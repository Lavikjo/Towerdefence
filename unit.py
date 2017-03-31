class Unit():

	def __init__(self, unit_type):
		self.pos = None
		self.world = None
		self.type = unit_type

	def get_pos(self):

		return self.pos

	def get_world(self):

		return self.world

	def get_type(self):

		return self.type

	def set_type(self, new_type):

		self.type = new_type

	def set_pos(self, pos):

		self.pos = pos

	def set_world(self, world, pos):

		if not world.get_square(pos).is_empty() or self.get_world() is not None:
			return False
		else:
			self.world = world
			self.pos = pos
			return True 

