import json
from people import people

with open('people.json', 'w') as people_json:
	json.dump(people, people_json, indent=2)
