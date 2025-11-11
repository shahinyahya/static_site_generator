from htmlnode import HTMLNode

class LeafNode(HTMLNode):
    def __init__(self, tag=None, value=None, children=None, props=None):
        super().__init__(tag, value, children, props)

    # if value is None:
    #     raise ValueError("All leaf nodes must have a value.")
    
    def to_html(self):
        
        if self.value is None:
            raise ValueError("All leaf nodes must render a value")
        
        if self.tag is None:
            return self.value

        #otherwise, render as HTML
        props_str = ""
        if self.props:
            props_str = " " + " ".join(f'{key}="{value}"' for key,value in self.props.items())
        
        return f"<{self.tag}{props_str}>{self.value}</{self.tag}>"