import pandas as pd
import requests
from bs4 import BeautifulSoup, NavigableString, Tag
import string


df = pd.read_excel('FreeEnglishTextbooks.xlsx')

for i, row in df.iterrows():

	authors = row['Author'].split(', ')
	surnames = []
	for author in authors:
		names = author.split()
		surnames.append(names[-1])

	title = row['Book Title']
	title += ' ' + str(row['Copyright Year']) + ' '
	title += ' '.join(surnames)

	whitelist = string.ascii_letters + string.digits + ' '
	title = ''.join([c for c in title if c in whitelist]).lower().replace(' ', '-')
	title += '.pdf'

	print('downloading ' + title + '...', end=' ')

	url = ''
	try:
		response = requests.get(row['OpenURL'])
		page = BeautifulSoup(response.text, 'html5lib')
		url = page.find('a', title="Download this book in PDF format")['href']
		url = 'https://link.springer.com' + url
		response = requests.get(url)

		with open('books/' + title, 'wb') as f:
			f.write(response.content)
		print('done.')
	except Exception as e:
		print('not found.', e)
