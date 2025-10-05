import os
from markdown_blocks import markdown_to_html_node, extract_title

def generate_page(from_path, template_path, dest_path):
    print(f"Generating page from {from_path} to {dest_path} using {template_path}")

    with open(from_path) as m: md = m.read()
    with open(template_path) as t: template = t.read()

    html_node = markdown_to_html_node(md)
    html_string = html_node.to_html()
    title = extract_title(md)

    new_html = template.replace("{{ Title }}", title)
    finished_html = new_html.replace("{{ Content }}", html_string)

    os.makedirs(os.path.dirname(dest_path), exist_ok=True)

    with open(dest_path, "w") as f: f.write(finished_html)