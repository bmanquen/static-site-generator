import unittest

from leafnode import LeafNode
from parentnode import ParentNode


class TestParentNode(unittest.TestCase):
    def test_single_parent(self):
        node = ParentNode(
            "p",
            [
                LeafNode("b", "Bold text"),
                LeafNode(None, "Normal text"),
                LeafNode("i", "italic text"),
                LeafNode(None, "Normal text"),
            ],
        )
        self.assertEqual(
            node.to_html(),
            "<p><b>Bold text</b>Normal text<i>italic text</i>Normal text</p>",
        )

    def test_single_nested_parents(self):
        node = ParentNode(
            "div",
            [
                ParentNode(
                    "p", [LeafNode("b", "Bold text"), LeafNode(None, "Normal text")]
                ),
                LeafNode("i", "italic text"),
                LeafNode(None, "Normal text"),
            ],
        )
        self.assertEqual(
            node.to_html(),
            "<div><p><b>Bold text</b>Normal text</p><i>italic text</i>Normal text</div>",
        )

    def test_multiple_nested_parents(self):
        node = ParentNode(
            "div",
            [
                ParentNode(
                    "p",
                    [
                        ParentNode(
                            "div", [LeafNode("a", "example", {"href": "example.com"})]
                        ),
                        LeafNode("b", "Bold text"),
                        LeafNode(None, "Normal text"),
                    ],
                ),
                LeafNode("i", "italic text"),
                LeafNode(None, "Normal text"),
            ],
        )
        self.assertEqual(
            node.to_html(),
            '<div><p><div><a href="example.com">example</a></div><b>Bold text</b>Normal text</p><i>italic text</i>Normal text</div>',
        )

    def test_no_children(self):
        node = ParentNode("div", None)
        with self.assertRaises(ValueError):
            node.to_html()

    def test_no_tags(self):
        node = ParentNode(None, None)
        with self.assertRaises(ValueError):
            node.to_html()
