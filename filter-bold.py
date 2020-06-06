from StyleFrame import StyleFrame
import pandas as pd

sf = StyleFrame.read_excel('FreeEnglishTextbooks.xlsx', read_style=True, use_openpyxl_styles=False)

ls = []
for row in sf.row_indexes:
	try:
		if sf.loc[row, 'Book Title'].style.bold:
			d = { 'Book Title': sf.loc[row, 'Book Title'].value, 
				'URL': sf.loc[row, 'OpenURL'].value }
			ls.append(d)
	except:
		pass
pd.DataFrame(ls).to_excel('filtered-books.xlsx')
