import requests

def fetch_data(url):
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    else:
        raise Exception(f"Failed to fetch data: {response.status_code}")

url = "https://api.github.com/users/yourusername/repos"
data = fetch_data(url)
print(data)
