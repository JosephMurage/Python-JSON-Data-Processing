# serialize Python object (dict) into JSON str
import json
# Python object (dictionary) to be serialized remember that the ''' at the beginning and end converts the JSON dict into a str
x = '''{
    "users": [
        {
            "status": {
                "text": "@jazzychad I just bought one .__."
            },
            "location": "San Francisco, California",
            "screen_name": "leahculver",
            "name": "Leah Culver"
        }
    ]
}
'''
py_data = json.loads(x)
leahculver = py_data ['users'] [0] ['name']
print (leahculver)
