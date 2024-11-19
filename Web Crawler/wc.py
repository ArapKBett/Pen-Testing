import requests
from bs4 import BeautifulSoup

def crawl(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    for link in soup.find_all('a'):
        print(link.get('href'))

url = 'http://example.com'
crawl(url)
