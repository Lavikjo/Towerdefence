#!/usr/bin/python3

from lxml import etree
import sys


plaindatafile = sys.argv[1]
xmldatafile = sys.argv[2]

root = etree.Element("map_data")
grid = etree.SubElement(root ,"map_grid")


try:
	with open(plaindatafile, 'r') as plain:
		x_counter = 0
		y_counter = 0
		for line in plain:
			print(line)
			map_width = len(line) - 1
			for char in line:
				if char == '\n':
					x_counter = 0
					break
				print(char)
				etree.SubElement(grid, "Square", x=str(x_counter), y=str(y_counter)).text = char
				x_counter += 1
			y_counter += 1
	etree.SubElement(root, "map_width").text = str(map_width)
	etree.SubElement(root, "map_height").text = str(y_counter)
	tree = etree.ElementTree(root)
	tree.write(xmldatafile, pretty_print = sys.argv[3])

except IOError:
	print("Failed opening files!")

