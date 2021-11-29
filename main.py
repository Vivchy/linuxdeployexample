import requests
from bs4 import BeautifulSoup


headers = {
    "Accept": "*/*",
    "User-Agent": "Mozilla/5.0 (iPad; CPU OS 11_0 like Mac OS X) AppleWebKit/604.1.34 (KHTML, like Gecko) Version/11.0 Mobile/15A5341f Safari/604.1"
}

url = 'https://www.youtube.com/'

req = requests.get(url, headers=headers)

print(req.status_code)
print('---------------------')
print(req.headers)
input('exit..........   ')
