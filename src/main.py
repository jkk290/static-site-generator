import os
import sys
from copystatic import copy_contents
from generatepage import generate_page_recursive

def main(argv):
    basepath = "/"
    if argv[1]:
        basepath = argv[1]

    project_root = os.path.dirname(os.path.dirname(__file__))
    src_dir = os.path.join(project_root, "static")
    dest_dir = os.path.join(project_root, "docs")
    copy_contents(src_dir, dest_dir, True)

    gen_src = os.path.join(project_root,"content")
    gen_tmp = os.path.join(project_root, "template.html")
    gen_dest = os.path.join(project_root, "docs")

    generate_page_recursive(gen_src, gen_tmp, gen_dest, basepath)


main(sys.argv)