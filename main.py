from enemy import *
from gameworld import *
from tower import * 
from mapreader import *

def main():

	#map_data = [[2, 2, 2, 2, 2], [0, 1, 2, 2, 2], [2, 1, 2, 2, 2], [2, 1, 2, 2, 2], [2, 3, 2, 2, 2]]
	#map_data2 = [[SquareType(x) for x in y] for y in map_data]
	world = MapReader.parse_map("default_map.xml")
	#world.waves = [{'LIGHT_ENEMY':2, 'HEAVY_ENEMIES':1}]
	tower1 = Tower(TowerType.BASIC_TOWER)
	tulos = world.add_tower(tower1, (1, 2))
	enemy1 = Enemy(EnemyType.LIGHT_ENEMY)
	enemy1.hp = 3
	world.add_enemy(enemy1, (3,0))
	#world.set_route([(1,0), (1,1), (2,1), (3,1), (4,1)])
	for i in range(7):
		enemy1.move()
		#tower1.attack(enemy1)
		print(enemy1.hp)
		print(enemy1.get_pos())
		print(world)
	print(enemy1.is_at_goal())

if __name__ == '__main__':
	main()