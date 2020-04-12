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

class EncounterRegion(BaseTable):
    def __init__(self, region: str):
         super().__init__('regions')
         

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

    def test_base_table_aint_no_fool(self):
        with self.assertRaises(ValueError):
            base_table = BaseTable('NOT A THING')

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

    def test_region_class_has_expected_attributes(self):
        test_region = EncounterRegion('port_vyshaan')
        #self.assertIsInstance(test_region.biomes, dict)
        pass

if __name__ == '__main__':
    unittest.main()
