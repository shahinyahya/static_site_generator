from src.textnode import TextType, TextNode
from src.leafnode import LeafNode
from src.htmlnode import HTMLNode

def text_node_to_html_node(text_node):
    if text_node.text_type == TextType.TEXT:
        return LeafNode(value=text_node.text)
    
    elif text_node.text_type == TextType.BOLD:
        return LeafNode(tag="b", value=text_node.text)
    
    elif text_node.text_type == TextType.ITALIC:
        return LeafNode(tag="i", value=text_node.text)
    
    elif text_node.text_type == TextType.CODE:
        return LeafNode(tag="code", value=text_node.text)

    elif text_node.text_type == TextType.LINK:
        if not text_node.url:
            raise ValueError("You must enter the link url")
        return LeafNode(tag="a", value=text_node.text, props={"href": text_node.url})
    
    elif text_node.text_type == TextType.IMAGE:
        if not text_node.url:
            raise ValueError("You must enter the image url")
        return LeafNode(tag="img", value="", props={"src": text_node.url, "alt": text_node.text})
    
    else:
        raise Exception(f"Unknown TextType: {text_node.text_type}")
