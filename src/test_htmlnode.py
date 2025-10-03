import unittest

from htmlnode import HTMLNode

class TestHTMLNode(unittest.TestCase):
    def test_repr(self):
        node = HTMLNode("h1", "Hello", None, {"href": "https://www.google.com", "target": "_blank"})
        self.assertEqual(
            "HTMLNode(h1, Hello, None, {'href': 'https://www.google.com', 'target': '_blank'})",
            repr(node)
        )
    
    def test_props_to_html(self):
        node = HTMLNode("h1", "Hello", None, {"href": "https://www.google.com", "target": "_blank"})
        self.assertEqual(
            " href=\"https://www.google.com\" target=\"_blank\"", node.props_to_html()
        )
    
    def test_has_children(self):
        node_child = HTMLNode("p", "Hi")
        node_parent = HTMLNode("div", None, [node_child])
        self.assertEqual(
            "HTMLNode(div, None, [HTMLNode(p, Hi, None, None)], None)", repr(node_parent)
        )

if __name__ == "__main__":
    unittest.main()