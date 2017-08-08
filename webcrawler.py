import bs4 as bs
import urllib.request

sauce = urllib.request.urlopen('').read()
soup = bs.BeautifulSoup(sauce, 'lxml')

#print(soup.find_all())

for paragraph in soup.find_all('p'):
	print(paragraph.text)
