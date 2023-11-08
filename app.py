import requests 
from json import dumps 

baseurl = "https://timeapi.io"
api_endpoint = "/api/Time/current/zone?timeZone=Europe/Amsterdam"

url = baseurl + api_endpoint
headers = {'accept': 'application/json'}

response = requests.request("GET", url, headers=headers)
print(response.text)
