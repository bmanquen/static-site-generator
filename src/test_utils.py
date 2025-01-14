import unittest

from textnode import TextNode, TextType
from utils import split_nodes_delimiter


class TestUtils(unittest.TestCase):
    def test_split_nodes_delimiter_invalid(self):
        with self.assertRaises(Exception):
            node = TextNode("This is text with a `code block word", TextType.TEXT)
            new_nodes = split_nodes_delimiter([node], "`", TextType.CODE)

    def test_split_nodes_delimiter_no_delimiter(self):
        node = TextNode("This is text with no delimiter characters", TextType.TEXT)
        new_nodes = split_nodes_delimiter([node], "`", TextType.CODE)
        self.assertEqual(new_nodes, [node])

    def test_split_nodes_delimiter_italic(self):
        node = TextNode("This is text with an *italic* word", TextType.TEXT)
        new_nodes = split_nodes_delimiter([node], "*", TextType.ITALIC)
        self.assertEqual(
            new_nodes,
            [
                TextNode("This is text with an ", TextType.TEXT),
                TextNode("italic", TextType.ITALIC),
                TextNode(" word", TextType.TEXT),
            ],
        )

    def test_split_nodes_delimiter_bold(self):
        node = TextNode("This is text with a **bold** word", TextType.TEXT)
        new_nodes = split_nodes_delimiter([node], "**", TextType.BOLD)
        self.assertEqual(
            new_nodes,
            [
                TextNode("This is text with a ", TextType.TEXT),
                TextNode("bold", TextType.BOLD),
                TextNode(" word", TextType.TEXT),
            ],
        )

    def test_split_nodes_delimiter_code(self):
        node = TextNode("this is text with a `code block` word", TextType.TEXT)
        new_nodes = split_nodes_delimiter([node], "`", TextType.CODE)
        self.assertEqual(
            new_nodes,
            [
                TextNode("this is text with a ", TextType.TEXT),
                TextNode("code block", TextType.CODE),
                TextNode(" word", TextType.TEXT),
            ],
        )

    def test_split_nodes_delimiter_multiple(self):
        node = TextNode(
            "this is text with a `code block` word and **bold** word", TextType.TEXT
        )
        new_nodes = split_nodes_delimiter([node], "`", TextType.CODE)
        new_nodes = split_nodes_delimiter(new_nodes, "**", TextType.BOLD)
        self.assertEqual(
            new_nodes,
            [
                TextNode("this is text with a ", TextType.TEXT),
                TextNode("code block", TextType.CODE),
                TextNode(" word and ", TextType.TEXT),
                TextNode("bold", TextType.BOLD),
                TextNode(" word", TextType.TEXT),
            ],
        )
