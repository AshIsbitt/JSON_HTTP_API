# Post with requests

# import requests
import json # standard from python

# json Standar library allows:
# .dumps() --> string that is json
# .dump() --> outputs a text file that is json

# filipe = {
#     'name': 'FILIPE PV',
#     'SuperPower': 'Patience...',
#     'prep level': 'wine and batteries for the xbox'
# }
#
# json.dump(str(filipe), 'filie_json')

# a Post needs:
# header and url
# json object

json_body = json.dumps({
"postcodes" : ["e147le", "SE172hy", "NE30 1DP", "N182aa"]
})
# print(type(json_body))

header = {'Content-type': 'application/json'}

url = "http://api.postcodes.io/postcodes/"

# Making POST api call with json_body, header and url
resq = requests.post(url, headers = header, data = json_body)

## working the request is exactly the same thing

response_json = resq.json()