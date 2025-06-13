#  Import libraries
import requests
from bs4 import BeautifulSoup

# Fetch the web page
url = 'https://edunetfoundation.org/'
response = requests.get(url)
if response.status_code == 200:
    print("Successfully fetched the web page!")

else:
    print(f"Failed to fetch the web page stauts code: {response.status_code} ")

# Task2:
# after fetching the HTML, we use beautifulsoup to parse it. We can extract various
#  type of data such as heading paragraphs links and images.

# Parce the Html content
soup = BeautifulSoup(response.text, 'lxml')

title = soup.title.string
print(f"page Title: (title)")
links = soup.find_all('a')
for link in links:
    href = link.get('href')
    text = link.get_text()
    print(f"link text : {text}, URL: {href}")

    # Extract all paragraphs
    paragraphs = soup.find_all('p')
    for paragraph in paragraphs:
        print(paragraph.get_text())
