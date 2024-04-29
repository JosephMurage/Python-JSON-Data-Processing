# Dictionaries nested within a list in a json file
import json

input = '''[
    {"id" : "001",
    "x" : "1",
    "name" : "Joseph Murage"
},
{"id" : "002",
"x" : "2",
"name" : "Friend"
}
]'''

info = json.loads (input) # info is a list in JS, not an object
print ('User count:', len(info)) # because it is a list, we can ask how many are there, and that's 2
for item in info: # iterate twice (since we have 2 nested dict) through the list and check the 2 nested dictionaries for...
    print ('Name:', item['name']) # names
    print ('Id:', item['id']) # ID
    print ('Attribute:', item['x']) # attribute