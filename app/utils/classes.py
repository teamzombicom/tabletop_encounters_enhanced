import unittest
import pathlib
import json
import random
from collections import defaultdict

BASE_DIRECTORY = pathlib.Path.cwd()
TABLES_DIRECTORY = BASE_DIRECTORY / 'app' / 'utils' / 'json_tables'

class BaseTable:
    def __init__(self, target_table):
        self.table_dir = TABLES_DIRECTORY.rglob(f'{target_table}/*')
        self.tables = {}
        for path in self.table_dir:
            with open(path) as table_contents:
                self.tables[path.stem] = json.load(table_contents)
        if self.tables.__len__() < 1:
            raise ValueError('No matching record')

    def getTables(self):
        return self.tables

class Trap(BaseTable):
    def __init__(self, trap_type: str):
        super().__init__('traps')
        self.trap_type = trap_type.capitalize().replace('_', '')
        self.save = self.tables[trap_type]['save']
        self.damage_type = self.tables[trap_type]['damage_type']
        self.good_reaction = self.tables[trap_type]['good_reaction']
        self.bad_reaction = self.tables[trap_type]['bad_reaction']
        self.fumble_injury = self.tables[trap_type]['fumble_injury']
        self.fumble_penalty = self.tables[trap_type]['fumble_penalty']

class EncounterRegion:
    def __init__(self, region_name: str):
        self.biomes = defaultdict(Biome)
        base_table = BaseTable('regions').tables
        for region in base_table:
            for biome_key in base_table[region]['biomes']:
                new_biome = Biome(biome_key)
                self.biomes[biome_key] = new_biome

    def rollBiome(self):
        biome_key = random.choice(list(self.biomes))
        return self.biomes[biome_key]

class Biome:
    def __init__(self, target_biome: str):
        base_table = BaseTable('biomes').tables
        self.display_name = base_table[target_biome]['display_name']
        self.terrain = base_table[target_biome]['terrain']
        self.obstacles = base_table[target_biome]['obstacles']
        self.bestiary = base_table[target_biome]['bestiary']
        self.climate = base_table[target_biome]['climate']
        self.loot_tables = base_table[target_biome]['loot_tables']
        self.foraging = base_table[target_biome]['terrain']

    def rollTerrain(self):
        return random.choice(list(self.terrain))

    def rollObstacles(self):
        return random.choice(list(self.obstacles))

    def rollBestiary(self):
        #TODO: Flesh out bestiary to include full stat block plus ultra
        #TODO; Maybe include enemy nummbers and common groupings and roll on tables from there
        #TODO; Add in What are the Monsters Doing roll
        #return random.choice(list(self.bestiary))
        return "Placeholder"

    def rollClimate(self):
        #TODO: Create base weather tables
        #TODO: Factor in humidity and temperature somehow
        #TODO: Allow for overrides from special weather
        #TODO: Return the result here
        return None#random.choice()

    def rollLoot(self):
        #TODO: Read in actual loot tables using the keys this class has at this point
        #TODO: Flesh out the structure of a random loot table to allow rollowing on that table
        #TODO: Return the result here
        return None#random.choice(self.loot_tables)

    def rollForaging(self):
        #TODO: Roll on each of the foraging tables and make a dict/list
        #TODO: Return the whole shebang here probably
        # Doesn't seem likely DM will do this often enough to need us to make them pick, they can roll 1d4 or whatever?
        return None#random.choice(list(self.foraging))

class ValidateTables:
    def __init__(self):
        table_directory = BASE_DIRECTORY.rglob('**/utils/json_tables/*')
        for table in table_directory:
            table_contents = table.rglob('*.json')
            for entry in table_contents:
                with open(entry) as raw_text:
                    json.load(raw_text)

class ClassesTest(unittest.TestCase):
    def test_base_table(self):
        base_table = BaseTable('biomes')
        self.assertIsInstance(base_table.tables['city'], dict)

    def test_base_table_fails_init_if_no_output(self):
        with self.assertRaises(ValueError):
            base_table = BaseTable('NOT A THING')
            if base_table is not None: pass

    def test_validate_all_json_tables_against_schema(self):
        table_directory = BASE_DIRECTORY.rglob('**/utils/json_tables/*')
        for table in table_directory:
            table_contents = table.rglob('*.json')
            for entry in table_contents:
                with open(entry) as raw_text:
                    #TODO: Implement Json Schema for these classes and verify here
                    result = json.load(raw_text)
                    self.assertIsNotNone(result)

    def test_trap_class_has_expected_attributes(self):
        base_trap = Trap('darts')
        self.assertEqual(base_trap.save, 'DEX')
        self.assertEqual(base_trap.damage_type, 'Piercing')
        self.assertEqual(base_trap.good_reaction, 'Prone')
        self.assertEqual(base_trap.bad_reaction, 'Jump')
        self.assertEqual(base_trap.fumble_injury, 'Puncture Wound')
        self.assertEqual(base_trap.fumble_penalty, '-1 Con')

    def test_biomes_class_has_expected_attributes(self):
        base_biome = Biome('salt_marsh')
        self.assertIsInstance(base_biome.display_name, str)
        self.assertIsInstance(base_biome.terrain, dict)
        self.assertIsInstance(base_biome.obstacles, dict)
        self.assertIsInstance(base_biome.bestiary, dict)
        self.assertIsInstance(base_biome.climate, dict)
        self.assertIsInstance(base_biome.loot_tables, list)
        self.assertIsInstance(base_biome.foraging, dict)

    def test_biomes_class_rolls_attributes(self):
        base_biome = Biome('salt_marsh')
        self.assertIsInstance(base_biome.rollTerrain(), str)
        self.assertIsInstance(base_biome.rollObstacles(), str)
        self.assertIsInstance(base_biome.rollBestiary(), str)
        self.assertIsNone(base_biome.rollClimate())
        self.assertIsNone(base_biome.rollLoot())
        self.assertIsNone(base_biome.rollForaging())

    def test_encounter_region_class_has_expected_attributes(self):
        test_region = EncounterRegion('port_vyshaan')
        self.assertIsInstance(test_region.biomes, dict)

    def test_encounter_region_class_returns_random_biomes(self):
        test_region = EncounterRegion('port_vyshaan')
        random_biome = test_region.rollBiome()
        self.assertIsInstance(random_biome, Biome)

if __name__ == '__main__':
    unittest.main()
