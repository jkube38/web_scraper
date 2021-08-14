from bs4 import BeautifulSoup
import requests
# just playing with bs4 before putting it into the webscraper
urls = set()
source = requests.get('http://www.imdb.com')
print(source.status_code)

# with open('test.html', 'r') as html:

soup = BeautifulSoup(source.text, 'lxml')
print('----relative anchor urls----')
for url in soup.find_all('a'):
    try:
        urls.add(url['href'])
    except KeyError:
        pass

print('----relative image urls----')
for url in soup.find_all('img'):
    urls.add(url['src'])

print(len(urls), urls(3))
# for url in urls:
#     print(url)
