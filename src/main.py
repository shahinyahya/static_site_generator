# from textnode import TextNode, TextType
from copy_static import copy_static
from generate_page import generate_page, generate_pages_recursive
import os
import shutil

def main():
    
    project_root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    static_dir = os.path.join(project_root, "static")
    public_dir = os.path.join(project_root, "public")
    content_index = os.path.join(project_root, "content")
    template_path = os.path.join(project_root, "template.html")

    # --- Delete public directory ---
    if os.path.exists(public_dir):
        shutil.rmtree(public_dir)

    # --- Recreate public directory ---
    os.makedirs(public_dir)

    copy_static(static_dir, public_dir)

    # Generate index.html
    # generate_page(
    #     from_path=content_index,
    #     template_path=template_path,
    #     dest_path=os.path.join(public_dir, "index.html")
    # )

    # Generate pages recursively
    generate_pages_recursive(dir_path_content=content_index, template_path=template_path, dest_dir_path=public_dir)

    print("Site generation complete.")

if __name__ == "__main__":
    main()