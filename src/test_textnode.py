import unittest

from leafnode import LeafNode
from textnode import TextNode, TextType


class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.BOLD)
        self.assertEqual(node, node2)

    def test_not_eq(self):
        node = TextNode("This is a test node", TextType.ITALIC)
        node2 = TextNode("This is a test", TextType.CODE)
        self.assertNotEqual(node, node2)

    def test_url_none(self):
        node = TextNode("This is a test", TextType.CODE)
        self.assertIsNone(node.url)

        node.url = "www.example.com"
        self.assertIsNotNone(node.url)

    def test_testtype_enum(self):
        with self.assertRaises(AttributeError):
            node = TextNode("this is a test", TextType.FAKE)

    def test_text_node_to_html_node_text(self):
        text_node = TextNode("This is a text node", TextType.TEXT)
        leaf_node = LeafNode(None, "This is a text node")
        self.assertEqual(
            TextNode.text_node_to_html_node(text_node).to_html(), leaf_node.to_html()
        )

    def test_text_node_to_html_node_image(self):
        text_node = TextNode("This is a text node", TextType.IMAGE, "example.com")
        leaf_node = LeafNode(
            "img", "", {"src": f"example.com", "alt": "This is a text node"}
        )
        self.assertEqual(
            TextNode.text_node_to_html_node(text_node).to_html(), leaf_node.to_html()
        )

    def test_text_node_to_html_node_bold(self):
        text_node = TextNode("This is a text node", TextType.BOLD)
        leaf_node = LeafNode("b", "This is a text node")
        self.assertEqual(
            TextNode.text_node_to_html_node(text_node).to_html(), leaf_node.to_html()
        )

    def test_text_node_to_html_node_italic(self):
        text_node = TextNode("This is a text node", TextType.ITALIC)
        leaf_node = LeafNode("i", "This is a text node")
        self.assertEqual(
            TextNode.text_node_to_html_node(text_node).to_html(), leaf_node.to_html()
        )

    def test_text_node_to_html_node_code(self):
        text_node = TextNode("This is a text node", TextType.CODE)
        leaf_node = LeafNode("code", "This is a text node")
        self.assertEqual(
            TextNode.text_node_to_html_node(text_node).to_html(), leaf_node.to_html()
        )

    def test_text_node_to_html_node_code(self):
        text_node = TextNode("This is a text node", TextType.LINK, "example.com")
        leaf_node = LeafNode("a", "This is a text node", {"href": "example.com"})
        self.assertEqual(
            TextNode.text_node_to_html_node(text_node).to_html(), leaf_node.to_html()
        )

    def test_text_node_to_html_node_invalid(self):

        with self.assertRaises(Exception):
            text_node = TextNode("This is a text node", TextType.FAKE, "example.com")
            TextNode.text_node_to_html_node(text_node)


if __name__ == "__main__":
    unittest.main()
