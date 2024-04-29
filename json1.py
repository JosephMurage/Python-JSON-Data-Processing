import json

data = '''{
"name": "Joseph Murage",
"phone": {
"type": "intl",
"number": "+254 724 498 506"
},
"email": {
"hide": "yes"
}
}'''

info = json.loads(data)
print ('Name:', info["name"])
print ("Phone Number:", info["phone"]["number"])
print ('Email Hidden:', info["email"]["hide"])