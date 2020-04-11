from urllib.parse import urlencode
from urllib import request, error
from app.utils import table_utils
import os
import unittest
import json

TEST_ENCOUNTER_REGIONS = { "city", "state"}

class Encounter:
    def __init__(self, region_dict: dict):
        self.values = { #TODO: tune self.values to reflect required fields and any defaults
            "regions": region_dict,
            "terrain": None,
            "terrain_description": None,
            "entities": None,
            "entity_tense": None,
            "encounter_time": None,
            "entity_motivation": None
        }

    def generate__new_encounter(self):
        #self.values[""] = ""
        return None

class EncounterTest(unittest.TestCase):
    def test_init_accepts_regional_encounter_dict(self):
        encounter = Encounter(TEST_ENCOUNTER_REGIONS)
        self.assertEqual(encounter.values["regions"], TEST_ENCOUNTER_REGIONS)
    def test_init_requires_dict_of_regions(self):
        with self.assertRaises(TypeError):
            encounter = Encounter()

            
if __name__ == '__main__':
    unittest.main()
    