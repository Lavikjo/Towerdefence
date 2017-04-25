from PyQt5.QtWidgets import QApplication
import sys

from enemy import *
from gameworld import *
from tower import * 
from mapreader import *
from gui import GUI

def main():
	world = MapReader.parse_map("default_map.xml")

	tower1 = Tower(TowerType.BASIC_TOWER)
	tulos = world.add_tower(tower1, (1, 1))
	tower2 = Tower(TowerType.BASIC_TOWER)
	world.add_tower(tower2, (1, 0))
	enemy1 = Enemy(EnemyType.LIGHT_ENEMY)
	world.add_enemy(enemy1, (3, 2))
	
	
	app = QApplication(sys.argv)
	gui = GUI(world, 30)

	app.exec_()
	app.deleteLater()
	sys.exit()

if __name__ == '__main__':
	main()