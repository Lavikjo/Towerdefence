from enemy import *
from gameworld import *
from tower import * 

def main():

	map_data = [[2, 2, 2, 2, 2], [0, 1, 2, 2, 2], [2, 1, 2, 2, 2], [2, 1, 2, 2, 2], [2, 3, 2, 2, 2]]
	map_data2 = [[SquareType(x) for x in y] for y in map_data]
	world = GameWorld(5, 5, map_data2)

	world.waves = [{'LIGHT_ENEMY':2, 'HEAVY_ENEMIES':1}]
	tower1 = Tower(TowerType.BASIC_TOWER)
	print(world.squares[0][0].square_type)
	tulos = world.add_tower(tower1, (0, 0))
	enemy1 = Enemy(EnemyType.LIGHT_ENEMY)
	world.add_enemy(enemy1, (1,1))
	print(world.squares[1][1].square_type)
	print(enemy1.type)
	print(tower1.type)
	print(world.squares[0][0].tower)
	print(world.towers[0].get_pos())
	print(world)

if __name__ == '__main__':
	main()