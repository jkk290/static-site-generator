import unittest

from textnode import TextNode, TextType

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

if __name__ == "__main__":
    unittest.main()