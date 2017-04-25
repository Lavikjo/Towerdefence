import xml.etree.ElementTree as ET
from square import SquareType
from gameworld import *

class MapReader():

	def parse_waves(root):
		waves = []
		for wave in root.find('waves'):
			waves.append(wave.attrib)
		return waves

	def parse_route(map_width, map_height, map_data):
		route = []

		for y in range(map_height):
			for x in range(map_width):
				#print(map_data[x][y])
				if map_data[x][y] in [SquareType.START_SQUARE, SquareType.ROUTE_SQUARE, SquareType.END_SQUARE]:
					route.append((x, y))
		#print(route)
		return route

	def parse_map(filename):
		root = ET.parse(filename).getroot()

		map_width = int(root[0].text)
		map_height = int(root[1].text)

		map_data = [None] * map_width
		for x in range(map_width):
			map_data[x] = [None] * map_height

		for square in root.find('map_grid'):
			#print(square.attrib, square.text)
			coords = square.attrib
			map_data[int(coords['x'])][int(coords['y'])] = SquareType(int(square.text))

		world = GameWorld(map_width, map_height, map_data)
		route = MapReader.parse_route(map_width, map_height, map_data)
		world.set_route(route)
		waves = MapReader.parse_waves(root)
		print(waves)
		world.set_waves(waves)

		return world

	