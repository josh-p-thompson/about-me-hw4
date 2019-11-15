import glob
import os
from jinja2 import Template

def generate_page_list(): 
    """ generate list of pages to be created based on presence in content directory """
    pages = []
    for file in glob.glob("content/*.html"): 
        file_name = os.path.basename(file)
        title, extension = os.path.splitext(file_name)
        if title == "index": 
            title = "About"
        pages.append(
            {
                'file_name': file_name, 
                'source': 'content/', 
                'destination': 'docs/', 
                'title': title.capitalize(), 
                title + '_btn': 'active',
            }
        )
    return pages

def generate_page(file_name, source, destination, title, pages): 
    """ generate pages from content and template and write to destination directory """
    template = Template(open('templates/base.html').read())
    full_page = template.render(
        title=title,
        file_name = file_name,
        destination=destination+file_name,
        right_block_content=open(source + file_name).read(), 
        pages=pages,
    )
    open(destination + file_name, 'w+').write(full_page)

def main(): 
    pages = generate_page_list()
    for page in pages:
        print(f'generating page {page}\n') 
        generate_page(
            file_name=page['file_name'],
            source=page['source'], 
            destination=page['destination'], 
            title=page['title'], 
            pages=pages,
        )

if __name__ == "__main__": 
    main()