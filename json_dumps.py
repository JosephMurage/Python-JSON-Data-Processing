# serialize Python object (dict) into JSON str
import json
# Python object (dictionary) to be serialized
python_dict = {'name': 'Joe', 'age': 31, 'city': 'Nairobi'}

# Serialize the Python object into a JSON formatted string
json_str = json.dumps(python_dict)

print (json_str)