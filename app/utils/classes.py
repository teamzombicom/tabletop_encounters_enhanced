import unittest
import pathlib
import json

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
        #print(region)
        #base_table = BaseTable(region)
        #for region in base_table.tables:
        #    print(region)
        self.biomes = {}
        self.terrain = {}
        base_table = BaseTable('regions').tables
        for region in base_table:
            for biome in base_table[region]['biomes']:
                new_biome = Biome(biome)
                self.terrain.update(new_biome.terrain)
        #print(base_table)
        #for region in base_table.tables:
            #biome_list = region['biomes']
            #for biome in region['biomes']:
            #print(biome_list)
            #pass

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
        #self.assertIsInstance(base_table.tables['city'], dict)

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

    def test_biomes_class_has_expected_attribrutes(self):
        base_biome = Biome('salt_marsh')
        self.assertIsInstance(base_biome.display_name, str)
        self.assertIsInstance(base_biome.terrain, dict)
        self.assertIsInstance(base_biome.obstacles, dict)
        self.assertIsInstance(base_biome.bestiary, dict)
        self.assertIsInstance(base_biome.climate, dict)
        self.assertIsInstance(base_biome.loot_tables, list)
        self.assertIsInstance(base_biome.foraging, dict)



    def test_region_class_has_expected_attributes(self):
        test_region = EncounterRegion('port_vyshaan')
        #self.assertIsInstance(test_region.biomes, dict)

if __name__ == '__main__':
    unittest.main()
