import pandas as pd
import requests
from bs4 import BeautifulSoup, NavigableString, Tag
import utils


df = pd.read_excel('FreeEnglishTextbooks.xlsx')

for i, row in df.iterrows():

	title = create_file_name(row)

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
