from PyQt5 import QtWidgets, QtCore, QtGui

class GUI(QtWidgets.QMainWindow):
	
	def __init__(self, world, square_size):
		super().__init__()
		self.setCentralWidget(QtWidgets.QWidget())
		self.horizontal = QtWidgets.QHBoxLayout()
		self.centralWidget().setLayout(self.horizontal)
		self.world = world
		self.square_size = square_size
		self.init_window()
		self.init_buttons()
		self.add_map_grid_items()
		self.add_tower_graphics_items()
		self.add_enemy_graphics_items()
		self.update_enemies()

		self.logic_timer = QtCore.QTimer()
		self.logic_timer.timeout.connect(self.update_enemies)
		self.logic_timer.start(10)

	def add_map_grid_items(self):
		pass

	def add_tower_graphics_items(self):
		pass

	def add_enemy_graphics_items(self):
		pass

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
		self.scene.setSceneRect(0, 0, 700, 700)

		self.view = QtWidgets.QGraphicsView(self.scene, self)
		self.view.adjustSize()
		self.view.show()
		self.horizontal.addWidget(self.view)
