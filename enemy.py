from enum import Enum
from square import Square, SquareType
from unit import Unit


class EnemyType(Enum):
	LIGHT_ENEMY = 0
	HEAVY_ENEMY = 1
	FAST_ENEMY = 2

class Enemy(Unit):

	def __init__(self, enemy_type):
		
		super(Enemy, self).__init__()
		self.type = enemy_type
