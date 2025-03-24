import requests

def get_data(url):
    response = requests.get(url)
    if response.status_code == 200:
        return response.text
    else:
        return f"Error: {response.status_code} - {response.text}"

url = "https://api.example.com/data"
data = get_data(url)
print(data)
