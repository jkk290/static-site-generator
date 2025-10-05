import os
import shutil
from textnode import TextNode, TextType

def main():
    project_root = os.path.dirname(os.path.dirname(__file__))
    src_dir = os.path.join(project_root, "static")
    dest_dir = os.path.join(project_root, "public")
    copy_contents(src_dir, dest_dir, True)

def copy_contents(src_dir, dest_dir, first_call):
    if not os.path.exists(src_dir):
        return
    
    if first_call and os.path.exists(dest_dir):
        shutil.rmtree(dest_dir)
        
    os.makedirs(dest_dir, exist_ok=True)

    dir_contents = os.listdir(src_dir)
    for content in dir_contents:
        content_src_path = os.path.join(src_dir, content)
        content_dest_path = os.path.join(dest_dir, content)
        if os.path.isfile(content_src_path):                
            shutil.copy(content_src_path, content_dest_path)
        elif os.path.isdir(content_src_path):
            copy_contents(content_src_path, content_dest_path, False)

main()