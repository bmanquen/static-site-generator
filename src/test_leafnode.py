import unittest

from leafnode import LeafNode


class TestLeafNode(unittest.TestCase):
    def test_to_html_no_tag(self):
        leaf_node = LeafNode(None, "this is a test")
        self.assertEqual(leaf_node.to_html(), "this is a test")

    def test_to_html_no_value(self):
        leaf_node = LeafNode(None, None)
        with self.assertRaises(ValueError):
            leaf_node.to_html()

    def test_to_html(self):
        leaf_node = LeafNode("a", "this is a test", {"href": "www.example.com"})
        self.assertEqual(
            leaf_node.to_html(),
            f"<{leaf_node.tag}{leaf_node.props_to_html()}>{leaf_node.value}</{leaf_node.tag}>",
        )


if __name__ == "__main__":
    unittest.main()
