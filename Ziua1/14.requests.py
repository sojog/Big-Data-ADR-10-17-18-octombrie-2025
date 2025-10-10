## pip install requests
import requests

response = requests.get("https://dummyjson.com/recipes")

print(response.status_code)
print(type(response.content))

print(type(response.json()))

