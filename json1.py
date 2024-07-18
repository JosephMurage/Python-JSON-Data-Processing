import json

data = '''{
"name": "Your Name",
"phone": {
"type": "intl",
"number": "Your PhoneNum"
},
"email": {
"hide": "yes"
}
}'''

info = json.loads(data)
print ('Name:', info["name"])
print ("Phone Number:", info["phone"]["number"])
print ('Email Hidden:', info["email"]["hide"])
