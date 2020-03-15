import requests

#Vars
path = "http://api.postcodes.io/postcodes/"
arguement = "SE172hy"
url = path + arguement

# Make request
resq = requests.get(url)

print(resq)
print(resq.status_code)
print(resq.headers)
print(resq.content)

#JSON Decoder
print(resq.json())

dict_post_code = resq.json()
print(type(dict_post_code))

