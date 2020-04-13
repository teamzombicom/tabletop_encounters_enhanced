import json
import jsonschema
import os 
import unittest
import pathlib
from app.utils import classes

def EncounterGenerator(region: str, biome: str =None):
    encounter_dict = {}
    encounter_region = classes.EncounterRegion(region)

    if biome == None:
        encounter_biome = classes.Biome('salt_marsh')#encounter_region.rollBiome()
    else:
        encounter_biome = classes.Biome(biome)
    encounter_dict['terrain'] = encounter_biome.rollTerrain()
    encounter_dict['obstacles'] = encounter_biome.rollObstacles()

    encounter_json = json.dumps(encounter_dict)
    return json.dumps(encounter_json)






class TableUtilitiesTest(unittest.TestCase):
    def test_encounter_generator_returns_expected_values(self):
        base_encounter = EncounterGenerator('port_vyshaan')
        
if __name__ == '__main__':
    unittest.main()

