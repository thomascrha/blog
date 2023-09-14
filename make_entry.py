import sys
from datetime import datetime

TEMPLATE="""
Title: {title}
Date: {year}-{month}-{day} {hour}:{minute:2d}
Tags:
Catergory:
Slug: {slug}
Summary:
Status: draft


"""
def make_entry(title):
    	today = datetime.today()
    	slug = title.lower().strip().replace(' ', '-')
    	f_create = "content/{}_{:0>2}_{:0>2}_{}.rst".format(
        	today.year, today.month, today.day, slug)
    	t = TEMPLATE.strip().format(title=title,
                                hashes='#' * len(title),
                                year=today.year,
                                month=today.month,
                                day=today.day,
                                hour=today.hour,
                                minute=today.minute,
                                slug=slug)
    	with open(f_create, 'w') as w:
		w.write(t)
	print("File created -> " + f_create)


if __name__ == '__main__':
	parser = argparse.ArgumentParser('helper script for creating new posts')

