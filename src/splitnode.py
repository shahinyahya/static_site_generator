from src.textnode import TextType,TextNode

'''
Here, we're using markup and this function turns markup to HTML. 
'''

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