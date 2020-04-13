import json
import jsonschema
import os 
import unittest
import pathlib
import classes

def EncounterGenerator(encounter_region: str):
    encounter_dict = {}
    region = classes.EncounterRegion(encounter_region)




    return json.dumps(encounter_json)






class TableUtilitiesTest(unittest.TestCase):
    def test_encounter_generator_returns_expected_values(self):
        base_encounter = EncounterGenerator('port_vyshaan')
        print(base_encounter)

        
if __name__ == '__main__':
    unittest.main()

