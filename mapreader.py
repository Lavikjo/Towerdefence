import xml.etree.ElementTree as ET
from square import SquareType

class MapReader():

	def parse_mapgrid(filename):
		root = ET.parse(filename).getroot()

		map_width = int(root[0].text)
		map_height = int(root[1].text)

		map_data = [None] * map_width
		for x in range(map_width):
			map_data[x] = [None] * map_height

		return map_data