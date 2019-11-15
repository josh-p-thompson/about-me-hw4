from string import Template

def generate_page(file_name, source, destination, title, about_btn="", projects_btn="", blog_btn=""): 
    """ generate pages from content and template and write to destination directory """
    template = Template(import_content('templates/base.html'))
    full_page = template.safe_substitute(
        title=title,
        right_block_content=import_content(source + file_name), 
        about_btn=about_btn, 
        projects_btn=projects_btn, 
        blog_btn=blog_btn,
    )
    open(destination + file_name, 'w+').write(full_page)

def import_content(file_path): 
    """ import content files """
    return open(file_path).read()

def main(): 
    pages = [
        {
            'file_name': 'index.html',
            'source_directory': 'content/',
            'destination_directory': 'docs/',
            'title': 'About', 
            'about_btn': 'active', 
        }, 
        {
            'file_name': 'projects.html',
            'source_directory': 'content/',
            'destination_directory': 'docs/',
            'title': 'Projects', 
            'projects_btn': 'active', 
        }, 
        {
            'file_name': 'blog.html',
            'source_directory': 'content/',
            'destination_directory': 'docs/',
            'title': 'Blog', 
            'blog_btn': 'active',
        }, 
    ]

    for page in pages:
        print(f'generating page {page}\n') 
        generate_page(
            file_name=page['file_name'],
            source=page['source_directory'], 
            destination=page['destination_directory'], 
            title=page['title'], 
            about_btn=page.get('about_btn'), 
            projects_btn=page.get('projects_btn'), 
            blog_btn=page.get('blog_btn'),
        )

if __name__ == "__main__": 
    main()