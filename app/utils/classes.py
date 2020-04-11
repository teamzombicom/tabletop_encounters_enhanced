import unittest
import pathlib
import json


class BaseTable:
    """
    A generic class which reads in json from root/utils/json_tables/TARGET_TYPE/TARGET_TABLE.json
    Makes the read in json available under self.values
    """
    def __init__(self, target_type: str, target_table: str=None):
        base_directory = pathlib.Path.cwd()
        tables_folder = base_directory.glob(f'json_tables/**/{target_type}/*.json')
        for matching_file in tables_folder:
            file_name = matching_file.name.replace('.json', '')
            if file_name == target_table:
                with open(matching_file) as target_table:
                    self.values = json.load(target_table)

class Trap(BaseTable):
    """
    An instance of BaseTable that makes all attributes of the specified Trap type available as attributes
    """
    def __init__(self, trap_type: str):
        super().__init__('misc', 'traps')
        self.trap_type = trap_type
        self.save = self.values[trap_type]['save']
        self.damage_type = self.values[trap_type]['damage_type']
        self.good_reaction = self.values[trap_type]['good_reaction']
        self.bad_reaction = self.values[trap_type]['bad_reaction']
        self.fumble_injury = self.values[trap_type]['fumble_injury']
        self.fumble_penalty = self.values[trap_type]['fumble_penalty']

class Region(BaseTable):
    def __init__(self, region: str):
         super().__init__('misc', 'regions')


class ClassesTest(unittest.TestCase):
    def test_trap_class_has_expected_attributes(self):
        dart_trap = Trap('darts')
        self.assertEqual(dart_trap.save, 'DEX')
        self.assertEqual(dart_trap.damage_type, 'Piercing')
        self.assertEqual(dart_trap.good_reaction, 'Prone')
        self.assertEqual(dart_trap.bad_reaction, 'Jump')
        self.assertEqual(dart_trap.fumble_injury, 'Puncture Wound')
        self.assertEqual(dart_trap.fumble_penalty, '-1 Con')

    def test_region_class_has_expected_attributes(self):
        test_region = Region('Port Vyshaan')
        pass

if __name__ == '__main__':
    unittest.main()