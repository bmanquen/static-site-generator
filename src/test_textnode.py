import unittest

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

if __name__ == "__main__":
    unittest.main()
