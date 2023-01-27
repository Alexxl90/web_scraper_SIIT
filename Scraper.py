import requests
from bs4 import BeautifulSoup
url = 'https://www.wowbiz.ro/'
word = input("Enter your keyword -->" )

page = requests.get(url)

if page.status_code == 200:
    soup = BeautifulSoup(page.content, 'html.parser')

    headers = soup.find_all(['h1', 'h2', 'h3', 'h4', 'h5', 'h6'])
    bodies = soup.find_all (['p', 'div'])
    results = headers + bodies


    results = soup.find_all(string=lambda text: word in text)

    with open("results.txt", "w", encoding= 'utf-8') as f:
        for result in results:
            f.write(result.get_text() + '\n')
else:
        print('Error')    



   