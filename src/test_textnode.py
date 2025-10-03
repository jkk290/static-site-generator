import unittest

from textnode import TextNode, TextType, text_node_to_html_node

class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a test node", TextType.BOLD)
        node2 = TextNode("This is a test node", TextType.BOLD)
        self.assertEqual(node, node2)

    def test_not_eq(self):
        node = TextNode("This is a test", TextType.TEXT)
        node2 = TextNode("this is another test", TextType.BOLD)
        self.assertNotEqual(node, node2)
    
    def test_url_none(self):
        node = TextNode("a link", TextType.LINK)
        self.assertIsNone(node.url)

    def test_url_not_none(self):
        node = TextNode("link!", TextType.LINK, "https://link.com")
        self.assertIsNotNone(node.url)

    def test_repr(self):
        node = TextNode("test repr", TextType.TEXT)
        self.assertEqual(
            "TextNode(test repr, text, None)",
            repr(node)
        )
    
    def test_text(self):
        node = TextNode("This is a text node", TextType.TEXT)
        html_node  = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, None)
        self.assertEqual(html_node.value, "This is a text node")
    
    def test_link_to_html(self):
        node = TextNode("click me", TextType.LINK, "https://link.com")
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, "a")
        self.assertEqual(html_node.value, "click me")
        self.assertEqual(html_node.props, {"href": "https://link.com"})
    
    def test_img_to_html(self):
        node = TextNode("an image", TextType.IMAGE, "https://link.com")
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, "img")
        self.assertEqual(html_node.props, {"src": "https://link.com", "alt": "an image"})

if __name__ == "__main__":
    unittest.main()