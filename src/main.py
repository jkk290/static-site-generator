import os
from copystatic import copy_contents
from generatepage import generate_page

def main():
    project_root = os.path.dirname(os.path.dirname(__file__))
    src_dir = os.path.join(project_root, "static")
    dest_dir = os.path.join(project_root, "public")
    copy_contents(src_dir, dest_dir, True)

    gen_src = os.path.join(project_root,"content/index.md")
    gen_tmp = os.path.join(project_root, "template.html")
    gen_dest = os.path.join(project_root, "public/index.html")

    glorfindel_src = os.path.join(project_root, "content/blog/glorfindel/index.md")
    glorfindel_dest = os.path.join(project_root, "public/blog/glorfindel/index.html")

    maj_src = os.path.join(project_root, "content/blog/majesty/index.md")
    maj_dest = os.path.join(project_root, "public/blog/majesty/index.html")

    tom_src = os.path.join(project_root, "content/blog/tom/index.md")
    tom_dest = os.path.join(project_root, "public/blog/tom/index.html")

    contact_src = os.path.join(project_root, "content/contact/index.md")
    contact_dest = os.path.join(project_root, "public/contact/index.html")

    generate_page(gen_src, gen_tmp, gen_dest)
    generate_page(glorfindel_src, gen_tmp, glorfindel_dest)
    generate_page(maj_src, gen_tmp, maj_dest)
    generate_page(tom_src, gen_tmp, tom_dest)
    generate_page(contact_src, gen_tmp, contact_dest)


main()