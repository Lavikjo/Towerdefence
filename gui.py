from PyQt5 import QtWidgets, QtCore, QtGui
from tower_graphics_item import TowerGraphicsItem
from enemy_graphics_item import EnemyGraphicsItem

class GUI(QtWidgets.QMainWindow):
	
	def __init__(self, world, square_size):
		super().__init__()
		self.setCentralWidget(QtWidgets.QWidget())
		self.horizontal = QtWidgets.QHBoxLayout()
		self.centralWidget().setLayout(self.horizontal)
		self.world = world
		self.square_size = square_size
		self.tower_graphics_items = []
		self.enemy_graphics_items = []


		self.init_window()
		self.init_buttons()
		self.add_map_grid_items()
		self.add_tower_graphics_items()
		self.add_enemy_graphics_items()
		self.update_logic()

		self.logic_timer = QtCore.QTimer()
		self.logic_timer.timeout.connect(self.update_logic)
		self.logic_timer.start(10)

		

	def add_map_grid_items(self):
		width = self.world.get_width()
		height = self.world.get_height()

		for x in range(width):
			for y in range(height):
				grid = QtWidgets.QGraphicsRectItem(x * self.square_size, y * self.square_size, self.square_size, self.square_size)
				square = self.world.get_square((x, y))
				if(square.is_start()):
					grid.setBrush(QtGui.QBrush(QtGui.QColor(20, 150, 0))) #Green
				elif(square.is_route()):
					grid.setBrush(QtGui.QBrush(QtGui.QColor(200, 130, 40))) #Brown
				elif(square.is_tower()):
					grid.setBrush(QtGui.QBrush(QtGui.QColor(90, 40, 0))) #Dark Brown
				else:
					grid.setBrush(QtGui.QBrush(QtGui.QColor(180, 0, 0))) #Red

				self.scene.addItem(grid)

	def add_tower_graphics_items(self):
		missing_towers = self.world.get_towers()
		for item in self.tower_graphics_items:
			if item.tower in missing_towers:
				missing_towers.remove(item.tower)
		for tower in missing_towers:
			tower_graphic = TowerGraphicsItem(tower, self.square_size)
			self.tower_graphics_items.append(tower_graphic)
			self.scene.addItem(tower_graphic)

	def add_enemy_graphics_items(self):
		missing_enemies = self.world.get_enemies()
		for item in self.enemy_graphics_items:
			if item.enemy in missing_enemies:
				missing_enemies.remove(item.enemy)
		for enemy in missing_enemies:
			enemy_graphic = EnemyGraphicsItem(enemy, self.square_size)
			self.enemy_graphics_items.append(enemy_graphic)
			self.scene.addItem(enemy_graphic)

	def update_logic(self):
		self.update_enemies()

	def update_enemies(self):
		pass

	def init_buttons(self):
		self.tower_btn = QtWidgets.QPushButton("Tower 1")
		self.horizontal.addWidget(self.tower_btn)

	def init_window(self):
		self.setGeometry(900, 900, 900, 900)
		self.setWindowTitle('Yet Another Tower Defense')
		self.show()

		self.scene = QtWidgets.QGraphicsScene()
		self.scene.setSceneRect(0, 0, 850, 850)

		self.view = QtWidgets.QGraphicsView(self.scene, self)
		self.view.adjustSize()
		self.view.show()
		self.horizontal.addWidget(self.view)
