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
                'source': file, 
                'destination': 'docs/' + file_name, 
                'title': title.capitalize(), 
            }
        )
    return sorted(pages, key = lambda page: page['title']) 

def generate_pages(pages): 
    """ generates pages from content/template and writes to destination directory """
    template = Template(open('templates/base.html').read())
    for page in pages: 
        print(f'generating page: {page}\n') 
        full_page = template.render(
            title= page['title'],
            file_name = page['file_name'],
            right_block_content=open(page['source']).read(), 
            pages=pages,
        )
        open(page['destination'], 'w+').write(full_page)

def main(): 
    pages = generate_page_list()
    generate_pages(pages)

if __name__ == "__main__": 
    main()