import requests

# GET request
# URL = path + arguments
# possibly the headers and metadata
# postcode.io --> follow their documentation
# capture the input --> decrypt JSON to dictionary
# Get some data out

# Variables for GET request:
path = "http://api.postcodes.io/postcodes/"
argument = 'SE172hy'
url = path + argument

# make the API call
resq = requests.get(url)

print(resq)
print(resq.status_code)
print(resq.headers)
print(resq.content)

## JSON decoder
print(resq.json())

dict_post_code = resq.json()
print(type(dict_post_code))

# Check how many keys?

## I want
# european_electoral_region
# outcode
# lng
# lat

# Make a little program that asks for a post code
# print back specific info


