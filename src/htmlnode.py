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