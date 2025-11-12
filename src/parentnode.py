from htmlnode import HTMLNode

class ParentNode(HTMLNode):
    def __init__(self, tag, children, props=None):
        if tag is None:
            raise ValueError("ParentNode must have a tag.")
        if not children:
            raise ValueError("ParentNode must have children.")
        super().__init__(tag=tag, value=None, children=children, props=props)


    def to_html(self):
        if self.tag is None:
            raise ValueError("Parent Node must have tags")
        
        if not self.children:
            raise ValueError("Parent Node must have children")
        
        #Build attributes string
        props_str = ""
        if self.props:
            props_str = " " + " ".join(f'{key}="{value}"' for key,value in self.props.items())

        #Recursively add children
        inner_html = "".join(child.to_html() for child in self.children)

        #Return Full HTMl
        return f"<{self.tag}{props_str}>{inner_html}</{self.tag}>"