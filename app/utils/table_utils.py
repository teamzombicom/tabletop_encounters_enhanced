import json
import jsonschema
import os 
import unittest
import pathlib
import classes





def TestTrap(self):
    test = classes.Trap('darts')
    #test = clasTrap('darts')
    print(test.save)

class TableUtilitiesTest(unittest.TestCase):
    def test_get_table_can_parse_all_listed_tables(self):
        testtarget = "darts"
        TestTrap(testtarget)

if __name__ == '__main__':
    unittest.main()

