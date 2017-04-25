import xml.etree.ElementTree as ET
from square import SquareType
from gameworld import *

class MapReader():

	def parse_mapgrid(filename):
		root = ET.parse(filename).getroot()

		map_width = int(root[0].text)
		map_height = int(root[1].text)

		map_data = [None] * map_width
		for x in range(map_width):
			map_data[x] = [None] * map_height

		for square in root.find('map_grid'):
			print(square.attrib, square.text)
			coords = square.attrib
			map_data[int(coords['y'])][int(coords['x'])] = SquareType(int(square.text))

		world = GameWorld(map_width, map_height, map_data)
		return world