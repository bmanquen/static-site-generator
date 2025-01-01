import unittest
from htmlnode import HTMLNode

class TestHTMLNode(unittest.TestCase):
    def test_props_to_html(self):
        html_node = HTMLNode(props = {"href": "https://www.example.com", "target": "_blank"})
        props_to_html = html_node.props_to_html()
        self.assertEqual(props_to_html, ' href="https://www.example.com" target="_blank"')

    def test_empty_props_to_html(self):
        html_node = HTMLNode(tag = 'p', value = "test")
        props_to_html = html_node.props_to_html()
        self.assertEqual(props_to_html, "")

    def test_repr(self):
        html_child_node = HTMLNode(tag = "p", value = "this is a child element")
        html_node = HTMLNode(tag = "div", value = "This is a div", children = [html_child_node] , props = {"target": "_blank"})
        self.assertEqual(html_node.__repr__(), f"HTMLNode({html_node.tag}, {html_node.value}, ['HTMLNode({html_child_node.tag}, {html_child_node.value}, {None}, {None})'], {html_node.props})")
