import unittest

from markdown_blocks import markdown_to_blocks, block_to_block_type


class TestMarkdownBlocks(unittest.TestCase):
    def test_markdown_to_blocks(self):
        markdown = """
# This is a heading

This is a paragraph of text. It has some **bold** and *italic* words inside of it.


* This is the first list item in a list block
* This is a list item
* This is another list item
"""
        block_strings = markdown_to_blocks(markdown)
        self.assertListEqual(
            block_strings,
            [
                "# This is a heading",
                "This is a paragraph of text. It has some **bold** and *italic* words inside of it.",
                "* This is the first list item in a list block\n* This is a list item\n* This is another list item",
            ],
        )
        
    def test_block_to_block_type_heading(self):
        markdown = "# This is a heading"
        block_strings = block_to_block_type(markdown)
        self.assertEqual(
            block_strings, "heading"
        )

    def test_block_to_block_type_code(self):
        markdown = "```This is a code block```"
        block_strings = block_to_block_type(markdown)
        self.assertEqual(
            block_strings, "code"
        )

    def test_block_to_block_type_quote(self):
        markdown = "> This is a quote block\n> with multipele\n> lines"
        block_strings = block_to_block_type(markdown)
        self.assertEqual(
            block_strings, "quote"
        )

    def test_block_to_block_type_unordered_list(self):
        markdown = "* This is the first list item in a list block\n* This is a list item\n* This is another list item"
        block_strings = block_to_block_type(markdown)
        self.assertEqual(
            block_strings, "unordered list"
        )

    def test_block_to_block_type_ordered_list(self):
        markdown = "1. This is the first list item in a list block\n2. is a list item\n3. is another list item"
        block_strings = block_to_block_type(markdown)
        self.assertEqual(
            block_strings, "ordered list"
        )

    def test_block_to_block_type_paragraph(self):
        markdown = "This is just a paragraph"
        block_strings = block_to_block_type(markdown)
        self.assertEqual(
            block_strings, "paragraph"
        )
