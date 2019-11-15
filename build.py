import glob
import os
from jinja2 import Template

def generate_page(file_name, source, destination, title, index_btn="", projects_btn="", blog_btn=""): 
    """ generate pages from content and template and write to destination directory """
    template = Template(open('templates/base.html').read())
    template.render(
        title=title,
        right_block_content=open(source + file_name).read(), 
        index_btn=index_btn, 
        projects_btn=projects_btn, 
        blog_btn=blog_btn,
    )

def generate_page_list(): 
    """ generate list of pages to be created based on presence in content directory """
    pages = []
    for file in glob.glob("content/*.html"): 
        file_name = os.path.basename(file)
        title, extension = os.path.splitext(file_name)
        pages.append(
            {
                'file_name': file_name, 
                'source_directory': 'content/', 
                'destination_directory': 'docs/', 
                'title': title.capitalize(), 
                title + '_btn': 'active',
            }
        )
    return pages

def main(): 
    pages = generate_page_list()
    for page in pages:
        print(f'generating page {page}\n') 
        generate_page(
            file_name=page['file_name'],
            source=page['source_directory'], 
            destination=page['destination_directory'], 
            title=page['title'], 
            index_btn=page.get('index_btn'), 
            projects_btn=page.get('projects_btn'), 
            blog_btn=page.get('blog_btn'),
        )

if __name__ == "__main__": 
    main()