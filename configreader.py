import xml.etree.ElementTree as ET

def convert(value):
	try:
		return int(value)
	except ValueError:
		return float(value)

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

	def parse_upgrades(upgrade_setting):
		upgrades = {}
		settings = {}

		for upgrade in upgrade_setting:
			converted_tuple = tuple([convert(x) for x in upgrade.text.split(',')])
			settings.update({(upgrade.tag, int(upgrade.attrib['level'])): converted_tuple})
		return settings

	def parse_towers(root):
		towers = {}
		settings = {}

		for tower in root.find('TowerData'):
			for setting in tower:
				if setting.tag == 'Upgrades':
					settings.update({setting.tag: ConfigReader.parse_upgrades(setting)})
				else:
					settings.update({setting.tag: setting.text})
				#Add parsing for updates later on here
			towers[tower.tag] = settings
			settings = {}
		#print(towers)
		return towers

	def parse_config(filename):
		configs = {}

		root = ET.parse(filename).getroot()
		configs["EnemyData"] = ConfigReader.parse_enemies(root)
		configs["TowerData"] = ConfigReader.parse_towers(root)
		return configs