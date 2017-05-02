from PyQt5 import QtWidgets, QtCore, QtGui
from tower_graphics_item import TowerGraphicsItem
from enemy_graphics_item import EnemyGraphicsItem
from tower import TowerType, Tower
from functools import partial

class QScene(QtWidgets.QGraphicsScene):
	def __init__(self, gui):
		QtWidgets.QGraphicsScene.__init__(self)
		self.gui = gui

	def mousePressEvent(self, ev):
		if ev.button() == QtCore.Qt.LeftButton:
			pos = ev.scenePos()
			unit = self.gui.selected_unit
			coord = (int(pos.x() / self.gui.square_size), int(pos.y() / self.gui.square_size))
			print(coord)
			try:
				square = self.gui.world.squares[coord[0]][coord[1]]
				if square.get_tower():
					self.gui.selection_label.setText("Selected tower: {}".format(coord))
					self.gui.selected_unit = None
				if unit:
					self.gui.selection_label.setText("")
					self.gui.selected_unit = None
					self.gui.world.add_tower(unit, coord)
			except IndexError:
				print("Click out of screen!")


class GUI(QtWidgets.QMainWindow):
	
	def __init__(self, world, square_size):
		super().__init__()
		self.main_widget = QtWidgets.QWidget()
		self.setCentralWidget(self.main_widget)
		self.horizontal = QtWidgets.QHBoxLayout()
		self.game_widget = QtWidgets.QWidget()
		self.side_widget = QtWidgets.QWidget()
		self.game_layout = QtWidgets.QHBoxLayout()

		self.horizontal.addWidget(self.game_widget)
		self.horizontal.addWidget(self.side_widget)
		self.centralWidget().setLayout(self.horizontal)

		self.button_layout = QtWidgets.QVBoxLayout()
		#self.button_layout.setColumnStretch(1, 20)

		self.side_widget.setLayout(self.button_layout)
		self.game_widget.setLayout(self.game_layout)

		self.world = world
		self.square_size = square_size
		self.tower_graphics_items = []
		self.enemy_graphics_items = []
		self.selected_unit = None

		self.init_window()
		self.init_buttons()
		self.add_map_grid_items()
		self.add_tower_graphics_items()
		self.add_enemy_graphics_items()

		self.logic_timer = QtCore.QTimer()
		self.logic_timer.timeout.connect(self.update_logic)
		self.logic_timer.start(200)

		self.graphic_timer = QtCore.QTimer()
		self.graphic_timer.timeout.connect(self.update_graphics)
		self.graphic_timer.start(1/60*1000)

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

	def remove_dead_graphics(self):
		for enemy_graphic in self.enemy_graphics_items:
			if not enemy_graphic.enemy.is_alive():
				self.scene.removeItem(enemy_graphic)
				self.enemy_graphics_items.remove(enemy_graphic)

	def update_all(self):
		self.update_logic()
		self.update_graphics()

	def update_graphics(self):
		self.add_tower_graphics_items()
		self.remove_dead_graphics()
		

		for enemy_graphic in self.enemy_graphics_items:
			enemy_graphic.update()
		for tower_graphic in self.tower_graphics_items:
			tower_graphic.update()

		self.update_labels()

	def update_labels(self):
		self.money_label.setText("Money: {}".format(self.world.money))

	def update_logic(self):
		self.update_enemies()

	def update_enemies(self):
		self.world.remove_dead_enemies()
		enemies = self.world.get_enemies()
		for enemy in enemies:
			if enemy.is_alive():
				enemy.move()

	def place_tower(self, tower_type):
		'''
		Sets spesific tower type as active unit
		'''

		self.selected_unit = Tower(tower_type)
		self.selection_label.setText("Selected: {}".format(tower_type).split(".")[-1])

	def init_buttons(self):

		self.tower_btn = QtWidgets.QPushButton("Electric")
		self.button_layout.addWidget(self.tower_btn)
		self.tower_btn.clicked.connect(partial(self.place_tower, TowerType.BASIC_TOWER))
		self.tower_btn2 = QtWidgets.QPushButton("Laser")
		self.tower_btn2.clicked.connect(partial(self.place_tower, TowerType.STRONG_TOWER))
		self.button_layout.addWidget(self.tower_btn2)

	def init_window(self):

		self.setGeometry(900, 900, 900, 640)
		self.setWindowTitle('Yet Another Tower Defense')
		self.show()

		self.scene = QScene(self)
		self.scene.setSceneRect(0, 0, 600, 600)

		self.view = QtWidgets.QGraphicsView(self.scene, self)
		self.view.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
		self.view.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
		self.view.adjustSize()
		self.view.show()

		self.game_layout.addWidget(self.view)

		self.money_label = QtWidgets.QLabel()
		self.selection_label = QtWidgets.QLabel()
		self.button_layout.addWidget(self.money_label)
		self.button_layout.addWidget(self.selection_label)