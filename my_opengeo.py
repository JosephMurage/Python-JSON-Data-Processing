import urllib.request, urllib.parse
import http, json, ssl

serviceurl = 'https://py4e-data.dr-chuck.net/opengeo?'

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False # do not check hostname
ctx.verify_mode = ssl.CERT_NONE # do not verify ssl certificate

while True:
    address = input ('Enter location: ')
    if len (address) <1: break
        
    address = address.strip()
    parms = dict () # parms is shortform for parameters
    parms ['q'] = address # 'q' is the new address parameter
    
    # encoding the parameters for easier reading on server side, for instance, comma and space are encoded into '%'
    url = serviceurl + urllib.parse.urlencode (parms) 
    
    print ('Retrieving', url)
    uh = urllib.request.urlopen (url, context=ctx) # retrieve the url based on parms defined above
    data = uh.read().decode() # read the data
    print ('Retrieved', len(data), 'characters', data[:20].replace('\n', '')) # len(data) calculates the number of chars in the decoded data object (in other words, length of the data str)
    
    js = json.loads(data) # parse json with .loads() to load the str object (data)
    
    # access the first feature in 'features' list of the json object 'js', then access its 'properties' dict nested therein, then retrieve the latitude value associated with the key 'lat'
    
    #print (json.dumps(js, indent = 4))
    #print (json.dumps(js['features'] [0] ['properties'] ['formatted']))

    lat = js['features'] [0] ['properties'] ['lat']
      # access the first feature in 'features' list of the json object 'js', access 'properties' dict therein, then retrieve the value associated with the 'lon' key in the 'properties' dict
    lon = js['features'] [0] ['properties'] ['lon']
      # print latitude and longitude values obtained from the 'js' object
    print ('latitude', lat, 'longitude', lon)
      # access the first feature of the 'features' list, then access the 'properties' dict therein, then retrieve the value associated with the key 'formatted' which has location info
    location = js['features'] [0] ['properties'] ['formatted']
    # print out the value of the key 'formatted' in other words, print the str object 'location' 
    print (location)