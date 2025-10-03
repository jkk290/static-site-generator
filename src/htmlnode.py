class HTMLNode:
    def __init__(self, tag=None, value=None, children=None, props=None):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props

    def to_html(self):
        raise NotImplementedError
    
    def props_to_html(self):
        if self.props is None:
            return ""
        props_keys = list(self.props.keys())
        props_values = list(self.props.values())
        html_string = ""
        for i in range(len(props_keys)):
            html_string += f" {props_keys[i]}=\"{str(props_values[i])}\""
        return html_string
    
    def __repr__(self):
        return f"HTMLNode({self.tag}, {self.value}, {self.children}, {self.props})"

class LeafNode(HTMLNode):
    def __init__(self, tag, value, props=None):
        super().__init__(tag, value, None, props)
    
    def to_html(self):
        if self.value is None:
            raise ValueError("leaves must have a value")
        elif self.tag is None:
            return f"{self.value}"
        else:
            props_string = super().props_to_html()
            return f"<{self.tag}{props_string}>{self.value}</{self.tag}>"
    
    def __repr__(self):
        return f"LeafNode({self.tag}, {self.value}, {self.props})"