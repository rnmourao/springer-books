import string

def create_file_name(row, extension='.pdf'):
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
    title += extension
    return title
