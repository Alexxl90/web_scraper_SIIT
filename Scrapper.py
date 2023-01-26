import requests
from bs4 import BeautifulSoup
url = 'https://www.hotnews.ro/'
word = 'Auditori'

page = requests.get(url)

if page.status_code == 200:
    soup = BeautifulSoup(page.content, 'html.parser')
    results = soup.find_all(string=lambda text: 'specific word' in text)

    for results in results:
        print(result)
    else:
        print('Error')    