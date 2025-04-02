import requests

def fetch_data(url):
    response = requests.get(url)
    if response.status_code == 200:
        return response.text
    else:
        raise Exception(f"Failed to fetch data from {url}")

# Example usage
url = "https://api.github.com/search/repositories?q=daily&sort=stars"
response_data = fetch_data(url)

if response_data:
    print(response_data)
else:
    print("Failed to fetch any data")
