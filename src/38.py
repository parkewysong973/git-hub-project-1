import requests
import json

url = "https://api.github.com/search/repositories?q=language:python&sort=stars"
response = requests.get(url)

if response.status_code == 200:
    data = response.json()
    
    stars_data = data["items"][0]["stargazers_count"]
    print(f"Star count of the repository: {stars_data}")
else:
    print("Failed to retrieve data from API")
