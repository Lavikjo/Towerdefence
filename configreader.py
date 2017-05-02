import xml.etree.ElementTree as ET

class ConfigReader:

	def parse_enemies(root):
		enemies = {}
		settings = {}

		for enemy in root.find('EnemyData'):
			for setting in enemy:
				settings.update({setting.tag: setting.text})
			enemies[enemy.tag] = settings
			settings = {}
		return enemies

	def parse_upgrades(upgrades):
		upgrades = {}
		settings = {}


	def parse_towers(root):
		towers = {}
		settings = {}

		for tower in root.find('TowerData'):
			for setting in tower:
				settings.update({setting.tag: setting.text})
				#Add parsing for updates later on here
			towers[tower.tag] = settings
			settings = {}
		return towers

	def parse_config(filename):
		configs = {}

		root = ET.parse(filename).getroot()
		configs["EnemyData"] = ConfigReader.parse_enemies(root)
		configs["TowerData"] = ConfigReader.parse_towers(root)

		return configs