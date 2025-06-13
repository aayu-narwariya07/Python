import requests
from bs4 import BeautifulSoup
import json

page = 1

qNum = 1
allQuotes = {}

for pageNum in range(1, 11):
    url = f'https://quotes.toscrape.com/page/{pageNum}/'

    response = requests.get(url)

    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'html.parser')
        quotes = soup.find_all('div', 'quote')
        
        for quote  in quotes:

            allQuotes[qNum] = {'Quote': quote.find('span', 'text').get_text(),
                               'Author': quote.find('small', 'author').get_text()
            }

            qNum += 1

    else:
        print('connection Faild', response.status_code)

with open('python\\lab61\\quotes.json', 'w') as QuotesFile:
    json.dump(allQuotes, QuotesFile)
