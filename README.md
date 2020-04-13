# README #

This is a Python 3.7 + Flask based app prototype. Ultimately, this app will allow for verbose random encounter generation populated from these json file templates:

* Region: A large geographical or contiguous adventuring area.
  * Example: A state, a walled city, a particular dungeon, or a demiplane
* Biome: Specific terrain, obstacles, climate, loot and foraging rewards, and bestiary entries that make up an encounter in a region
  * Example: The general region of the German state of Bavaria has forests, cities, suburbs, and possibly mountains, each of which has different sorts of encounters.
* Bestiary: Entries for possible enemies or other NPCs that may be encountered in a biome
* Item Tables: The loot tables for the biomes
* Foraging tables: For overland exploration in a biome, foraging may yield these items
* Obstacles: Biome specific challenges/hazards that cause dramatic tension or modify combat scenarios.

Often, a dungeon master may roll in a bestiary for random encounters, and if they have time they might check weather. Locations are often a flat, arbitrarily large square, and loot is rolled afterward and appears from nowhere, from enemies that were presumably standing in the open waiting for the party. Weather and time of day, which change throughout an adventuring day, might often be ignored altogether. With this system, even a small number of variance in individual components can make for much more memorable and yet convenient scenarios for the lazy gm.

## How do I get set up? ##

* Clone the repository
* Install dependencies | pip install -r requirements.txt
* Run the application | flask run
* Navigate to http://127.0.0.1:5000/encounters/port_vyshaan

## Contribution guidelines ##

* Write unit tests
* Run unit tests
* Stick to the file pattern of app/utils/json_table/{table directory}/{table entry.json}
* Run the classes.py file after adding new json or tables; it validates all json
* The existing app structure can be run nicely with VS Code or Pycharm. 

### TODO ###

* Get unit tests running as a whole and in an automated fashion
* Better package management
* Build out weather system
* Convert bestiary/srd_5e_monsters.json to fit our needs
* Build out foraging and item tables
* More and handier flask routes
* Flesh out more biomes and regions
* Initialize SQLLite DB and convert json_tables
* Adapt table utils to read in from DB instead of json_tables dir
