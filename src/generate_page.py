import os
from markdown_to_html import markdown_to_html_node
from extract_markdown_html import extract_title

def generate_page(from_path, template_path, dest_path):
    print(f"Generating page from {from_path} to {dest_path} using {template_path}")

    # Read markdown file
    with open(from_path, "r") as f:
        markdown = f.read()
    
    # Read template file
    with open(template_path, "r") as f:
        template = f.read()
    
    # Convert markdown -> HTML
    html_node = markdown_to_html_node(markdown)
    html_content = html_node.to_html()

    # Extract markdown title
    title = extract_title(markdown)

    # Replace placeholders
    final_html = template.replace("{{ Title }}", title).replace("{{ Content }}", html_content)

    # Ensure directory exists
    os.makedirs(os.path.dirname(dest_path), exist_ok=True)

    # Write output
    with open(dest_path, "w") as f:
        f.write(final_html)

# Function to generate pages recursively
def generate_pages_recursive(dir_path_content, template_path, dest_dir_path):

    # Walk through every paths
    for entry in os.listdir(dir_path_content):
        entry_path = os.path.join(dir_path_content, entry)
        dest_path = os.path.join(dest_dir_path, entry)

        # If it's a directory → recursively process
        if os.path.isdir(entry_path):
            os.makedirs(dest_path, exist_ok=True)
            generate_pages_recursive(entry_path, template_path, dest_path)
        
        # If it's a markdown file → convert to html
        elif entry_path.endswith(".md"):
            html_filename = entry.replace(".md", ".html")
            dest_file = os.path.join(dest_dir_path, html_filename)

            generate_page(entry_path, template_path, dest_file)
