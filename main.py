from enemy import *
from gameworld import *
from tower import * 

def main():

	map_data = [[2, 2, 2, 2, 2], [0, 1, 2, 2, 2], [2, 1, 2, 2, 2], [2, 1, 2, 2, 2], [2, 3, 2, 2, 2]]
	map_data2 = [[SquareType(x) for x in y] for y in map_data]
	world = GameWorld(5, 5, map_data2)

	world.waves = [{'LIGHT_ENEMY':2, 'HEAVY_ENEMIES':1}]
	tower1 = Tower(TowerType.BASIC_TOWER)
	tulos = world.add_tower(tower1, (0, 0))
	enemy1 = Enemy(EnemyType.LIGHT_ENEMY)
	world.add_enemy(enemy1, (1,0))
	world.set_route([(1,0), (1,1), (2,1), (3,1), (4,1), (5,1)])
	for i in range(5):
		print(enemy1.get_pos())
		print(world)
		enemy1.move()

if __name__ == '__main__':
	main()