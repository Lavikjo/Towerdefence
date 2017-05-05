import xml.etree.ElementTree as ET
from square import SquareType
from gameworld import *

class MapReader():

	def parse_waves(root):
		'''
		Parse wave related data
		'''
		waves = []
		for wave in root.find('waves'):
			waves.append({key: int(value) for (key, value) in wave.attrib.items()})
		return waves

	def parse_route(world, map_data):
		'''
		Finds route from map
		'''
		route = []
		start_square = world.get_start_square()
		route.append(start_square)
		previous_pos = start_square
		current_pos = previous_pos
		neigbours = [(1, 0), (0, 1), (-1, 0), (0, -1)]

		# loop until end is found
		while map_data[current_pos[0]][current_pos[1]] is not SquareType.END_SQUARE:
			# generate neighbour coordinates in cardinal directions relative to current position
			neighbour_coordinates = [tuple(map(sum, zip(current_pos, coord))) for coord in neigbours]
			
			# check if neighbour coordinates contain valid route square
			for x in neighbour_coordinates:
				if x != previous_pos and world.get_square(x).square_type in [SquareType.ROUTE_SQUARE, SquareType.END_SQUARE]:
					route.append(x)
					break

			previous_pos = current_pos
			current_pos = x
					
		return route

	def parse_map(filename):
		'''
		Parse map grid data
		'''
		try:
			root = ET.parse(filename).getroot()

			map_width = int(root[0].text)
			map_height = int(root[1].text)

			map_data = [None] * map_width
			for x in range(map_width):
				map_data[x] = [None] * map_height

			for square in root.find('map_grid'):
				coords = square.attrib
				map_data[int(coords['x'])][int(coords['y'])] = SquareType(int(square.text))

			world = GameWorld(map_width, map_height, map_data)
			route = MapReader.parse_route(world, map_data)
			world.set_route(route)
			waves = MapReader.parse_waves(root)
			world.set_waves(waves)
			
		except ET.ParseError:
			print("Corrupted map file!")
			return False
		return world

	