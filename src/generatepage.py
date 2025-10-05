import os
from markdown_blocks import markdown_to_html_node, extract_title

def generate_page(from_path, template_path, dest_path, basepath):
    print(f"Generating page from {from_path} to {dest_path} using {template_path}")

    with open(from_path) as m: md = m.read()
    with open(template_path) as t: template = t.read()

    html_node = markdown_to_html_node(md)
    html_string = html_node.to_html()
    title = extract_title(md)

    new_html = template.replace("{{ Title }}", title)
    new_html = new_html.replace("{{ Content }}", html_string)

    new_html = new_html.replace("href=\"/", f"href=\"{basepath}")
    finished_html = new_html.replace("src=\"/", f"src=\"{basepath}")

    os.makedirs(os.path.dirname(dest_path), exist_ok=True)

    with open(dest_path, "w") as f: f.write(finished_html)

def generate_page_recursive(dir_path_content, template_path, dest_dir_path, basepath):
    if not os.path.exists(dir_path_content):
        return
    
    dir_contents = os.listdir(dir_path_content)
    for content in dir_contents:
        content_src_path = os.path.join(dir_path_content, content)

        if os.path.isdir(content_src_path):
            new_dest_dir_path = os.path.join(dest_dir_path, content)
            generate_page_recursive(content_src_path, template_path, new_dest_dir_path, basepath)
        else:
            dest_content = content.replace(".md", ".html")
            content_dest_path = os.path.join(dest_dir_path, dest_content)

            print(f"Generating page from {content_src_path} to {content_dest_path} using {template_path}")

            with open(content_src_path) as m: md = m.read()
            with open(template_path) as t: template = t.read()

            html_node = markdown_to_html_node(md)
            html_string = html_node.to_html()
            title = extract_title(md)

            new_html = template.replace("{{ Title }}", title)
            new_html = new_html.replace("{{ Content }}", html_string)

            new_html = new_html.replace("href=\"/", f"href=\"{basepath}")
            finished_html = new_html.replace("src=\"/", f"src=\"{basepath}")

            os.makedirs(os.path.dirname(content_dest_path), exist_ok=True)

            with open(content_dest_path, "w") as f: f.write(finished_html)
