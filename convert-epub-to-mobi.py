import os


from_dir = '/home/mourao/livros/springer-books/epub/'
to_dir = '/home/mourao/livros/springer-books/mobi/'

files = os.listdir(from_dir)

for file in files:
    mobi = file.replace('.epub', '.mobi')
    print('converting ' + mobi + '...', end=' ')
    os.system('ebook-convert ' + 
            os.path.join(from_dir, file) + ' ' + os.path.join(to_dir, mobi))
    print('done.')