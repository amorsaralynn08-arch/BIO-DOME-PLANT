#using a free API  for weather handling , no keys needed
import requests
url = "https://api.open-meteo.com/v1/forecast?latitude=-1.2833&longitude=36.8167&current=temperature_2m,relative_humidity_2m"
response = requests.get(url) #getting the data
data = response.json
