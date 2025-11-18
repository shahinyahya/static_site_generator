import re

from src.textnode import TextType,TextNode

'''
Here, we're using markup and this function turns markup to HTML. 
'''

# Regex patterns:
# Link:  [text](url)
LINK_PATTERN = re.compile(r"\[([^\]]+)\]\(([^)]+)\)")
# Image: ![alt](url)
IMAGE_PATTERN = re.compile(r"!\[([^\]]*)\]\(([^)]+)\)")

def split_nodes_delimiter(old_nodes, delimiter, text_type):

    # Create a new nodes list
    new_nodes = []

    for node in old_nodes:
        if node.text_type != TextType.TEXT:
            new_nodes.append(node)
            continue

        text = node.text
        parts = text.split(delimiter)

        # If there is no delimitter, keep it as is.
        if len(parts) == 1:
            new_nodes.append(node)
            continue

        # Valid markdowm need even number of delimitter, i.e, if there's no ending delimitters.
        if len(parts) % 2 == 0:
            raise Exception(f"Invalid Markdown: missing closing delimiter '{delimiter}' in text: {text}")
        
        for i, segment in enumerate(parts):
            if segment == "":
                # if it is like `` this skip it
                continue

            if i % 2 == 0:
                new_nodes.append(TextNode(segment, TextType.TEXT))
            else:
                # Odd index, inside delimiters etc..
                new_nodes.append(TextNode(segment, text_type))
    
    return new_nodes

def split_nodes_image(old_nodes):
    
    new_nodes = []

    for node in old_nodes:
        #Only split text nodes.
        if node.text_type != TextType.TEXT:
            new_nodes.append(node)
            continue
        
        text = node.text
        matches = list(IMAGE_PATTERN.finditer(text))

        if not matches:
            new_nodes.append(node)
            continue

        last_index = 0

        for match in matches:
            start, end = match.span()
            alt, url = match.group(1), match.group(2)

            # Add text before image
            if start > last_index:
                new_nodes.append(TextNode(text[last_index:start], TextType.TEXT))
            
            # Add image node
            new_nodes.append(TextNode(alt, TextType.IMAGE, url))

            last_index = end
        
        # Add remaining text after last match
        if last_index < len(text):
            new_nodes.append(TextNode(text[last_index:], TextType.TEXT))
    
    return new_nodes

def split_nodes_link(old_nodes):
    
    new_nodes = []

    for node in old_nodes:
        # Only text nodes.
        if node.text_type != TextType.TEXT:
            new_nodes.append(node)
            continue
    
        text = node.text
        matches = list(LINK_PATTERN.finditer(text))

        if not matches:
            new_nodes.append(node)
            continue

        last_index = 0

        for match in matches:
            start, end = match.span()
            label, url = match.group(1), match.group(2)

        # Add text before link
        if start > last_index:
            new_nodes.append(TextNode(text[last_index:start], TextType.TEXT))

        # Add the link node
        new_nodes.append(TextNode(label, TextType.LINK, url))

        last_index = end

        # Add remaining text after last match
        if last_index < len(text):
            new_nodes.append(TextNode(text[last_index:], TextType.TEXT))

    return new_nodes