import requests

# GET request
# URL = path + arguments
# postcode.io --> follow their documentation
# capture the input --> decrypt JSON to dictionary
# Get some data out

# Variables for GET request:
path = "http://api.postcodes.io/postcodes/"
argument = 'SE172hy'
url = path + argument

# make the API call
requests.get(url)

