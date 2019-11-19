import glob
import os
from jinja2 import Template
import markdown

def generate_page_list(): 
    pages = []
    for directory in glob.glob("content/*"): 
        title = os.path.basename(directory)
        file_name = title + ".html"
        if title == 'index': 
            title = 'about'
        cards = [markdown_to_html(file) for file in glob.glob(directory + "/*.md")]
        pages.append(
            {
                'file_name': file_name, 
                'source': directory + "/", 
                'destination': 'docs/' + file_name, 
                'title': title, 
                'cards': cards,
            }
        )
    return sorted(pages, key = lambda page: page['title']) 

def markdown_to_html(file): 
    """
    imports card files and returns dictionary with top and bottom sections of card
    """
    md = markdown.Markdown(extensions=["markdown.extensions.meta", "markdown.extensions.attr_list", "markdown.extensions.extra"])
    data = open(file).read()
    html = md.convert(data)
    card = {'top': html.split('<hr />')[0], 'bottom': html.split('<hr />')[1]}
    return card

def build_pages(pages): 
    template = Template(open('templates/base.html').read())
    for page in pages: 
        print(f'generating page: {page}\n') 
        full_page = template.render(
            title = page['title'],
            file_name = page['file_name'],
            cards = page['cards'],
            pages=pages,
        )
        open(page['destination'], 'w+').write(full_page)


def main(): 
    pages = generate_page_list()
    build_pages(pages)

if __name__ == "__main__": 
    main()