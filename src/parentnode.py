from htmlnode import HTMLNode

class ParentNode(HTMLNode):
    def __init__(self, tag, children, props=None):
        super().__init__(tag, children, props)

    def to_html(self):
        if self.tag is None:
            raise ValueError("Parent Node must have tags")
        
        if not self.children:
            raise ValueError("Parent Node must have children")
        
        
        
