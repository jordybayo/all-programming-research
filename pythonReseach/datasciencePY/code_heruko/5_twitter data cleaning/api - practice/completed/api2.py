import requests, json 
  
# Enter your API key here 
api_key = "220337f18a8eb69162f1218ff80e55f0"
  
# base_url variable to store url 
base_url = "https://api.openweathermap.org/data/2.5/weather"
  
payload = {
    "appid": api_key, 
    "q": "mumbai", 
}
  
response = requests.get(base_url,params=payload)
  
response = response.json() 
  
print(response)
print("Weather: ",response["weather"][0]["description"])
