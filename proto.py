import requests
from bs4 import BeautifulSoup

response = requests.get('https://news.google.com/?hl=en-IN&gl=IN&ceid=IN%3Aen')
soup = BeautifulSoup(response.text, 'html.parser')

rawData = soup.find_all('a', {'class': 'ipQwMb'})

with open('result.text','a') as file:
	for i in rawData:
		file.write(i.span.text)
		file.write("\n\n")
