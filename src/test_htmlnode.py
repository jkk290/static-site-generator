import unittest

from htmlnode import HTMLNode, LeafNode, ParentNode

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
    
    def test_leaf_to_html_p(self):
        node = LeafNode("p", "Hello, world!")
        self.assertEqual(node.to_html(), "<p>Hello, world!</p>")
    
    def test_leaf_to_html_props(self):
        node = LeafNode("a", "Hello, world!", {"href": "https://hello.com"})
        self.assertEqual(node.to_html(), '<a href="https://hello.com">Hello, world!</a>')
    
    def test_leaf_repr(self):
        node = LeafNode("p", "hi")
        self.assertEqual(repr(node), "LeafNode(p, hi, None)")
    
    def test_to_html_with_children(self):
        child_node = LeafNode("span", "child")
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(parent_node.to_html(), "<div><span>child</span></div>")
    
    def test_to_html_with_grandchildren(self):
        grandchild_node = LeafNode("b", "grandchild")
        child_node = ParentNode("span", [grandchild_node])
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(
            parent_node.to_html(),
            "<div><span><b>grandchild</b></span></div>"
        )
    
    def test_to_html_no_children(self):
        parent_node = ParentNode("div", [])
        with self.assertRaises(ValueError):
            parent_node.to_html()

if __name__ == "__main__":
    unittest.main()