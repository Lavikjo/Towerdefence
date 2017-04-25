from enemy import *
from gameworld import *
from tower import * 
from mapreader import *

def main():
	world = MapReader.parse_map("default_map.xml")

	tower1 = Tower(TowerType.BASIC_TOWER)
	tulos = world.add_tower(tower1, (1, 2))
	enemy1 = Enemy(EnemyType.LIGHT_ENEMY)
	enemy1.hp = 3
	world.add_enemy(enemy1, (3, 0))
	for i in range(5):
		enemy1.move()
		tower1.attack(enemy1)
		#print(enemy1.get_pos())
		print(world)
	#print(enemy1.is_at_goal())

if __name__ == '__main__':
	main()