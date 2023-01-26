import requests
from bs4 import BeautifulSoup
url = 'https://stirileprotv.ro/'
word = input("Enter your keyword -->" )

page = requests.get(url)

if page.status_code == 200:
    soup = BeautifulSoup(page.content, 'html.parser')
    results = soup.find_all(string=lambda text: word in text)

    for results in results:
        print(results)
    else:
        print('Error')    