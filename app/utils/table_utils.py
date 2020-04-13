import json
import jsonschema
import os 
import unittest
import pathlib
from app.utils import classes

def EncounterGenerator(region: str):
    encounter_dict = {}
    encounter_region = classes.EncounterRegion(region)
    encounter_biome = classes.Biome('salt_marsh')#encounter_region.rollBiome()
    
    encounter_dict['terrain'] = encounter_biome.rollTerrain()
    encounter_dict['obstacles'] = encounter_biome.rollObstacles()

    encounter_json = json.dumps(encounter_dict)
    return json.dumps(encounter_json)






class TableUtilitiesTest(unittest.TestCase):
    def test_encounter_generator_returns_expected_values(self):
        base_encounter = EncounterGenerator('port_vyshaan')
        
if __name__ == '__main__':
    unittest.main()

