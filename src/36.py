import requests
from bs4 import BeautifulSoup

def get_hobbies():
    url = "https://www.example.com/eng/hobby"
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    
    hobbies_list = [li.text for li in soup.select('.hobby-list li') if li.get('class') == ['active']]
    
    return hobbies_list

if __name__ == "__main__":
    print(get_hobbies())
