import urllib.request, urllib.parse
import http, json, ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

serviceurl = 'https://py4e-data.dr-chuck.net/comments_2014520.json'

while True:
    url = urllib.request.urlopen (serviceurl, context=ctx) # retrieve the url based on parms defined above
    data = url.read().decode() # read the data
    
    # Parse JSON data
    js = json.loads(data)
    print('Error parsing JSON data.')
        
    # count number of comments from item list in the js file    
    comment_counts = [int(item['count']) for item in js['comments']]
    total_comments = sum(comment_counts)
    print ('Retrieved', total_comments)



data = urllib.request.urlopen (url, context=ctx)
