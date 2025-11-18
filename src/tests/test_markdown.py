import unittest

from src.markdown_function import markdown_to_blocks, BlockType, block_to_block_type

class TestMarkDownToBlocks(unittest.TestCase):
    def test_markdown_to_blocks(self):
        md = """
This is **bolded** paragraph

This is another paragraph with _italic_ text and `code` here
This is the same paragraph on a new line

- This is a list
- with items
"""
        blocks = markdown_to_blocks(md)
        self.assertEqual(
            blocks,
            [
                "This is **bolded** paragraph",
                "This is another paragraph with _italic_ text and `code` here\nThis is the same paragraph on a new line",
                "- This is a list\n- with items",
            ],
        )

    def test_heading(self):
        assert block_to_block_type("# Heading") == BlockType.HEADING
        assert block_to_block_type("###### Six level heading") == BlockType.HEADING


    def test_code_block(self):
        block = "```\nprint('hello')\n```"
        assert block_to_block_type(block) == BlockType.CODE


    def test_quote_block(self):
        block = "> quote line 1\n> quote line 2"
        assert block_to_block_type(block) == BlockType.QUOTE


    def test_unordered_list(self):
        block = "- item 1\n- item 2\n- item 3"
        assert block_to_block_type(block) == BlockType.UNORDERED_LIST


    def test_ordered_list_valid(self):
        block = "1. first\n2. second\n3. third"
        assert block_to_block_type(block) == BlockType.ORDERED_LIST


    def test_ordered_list_invalid_not_incrementing(self):
        block = "1. first\n3. wrong"
        assert block_to_block_type(block) == BlockType.PARAGRAPH


    def test_ordered_list_invalid_missing_dot(self):
        block = "1 first\n2 second"
        assert block_to_block_type(block) == BlockType.PARAGRAPH


    def test_paragraph_default(self):
        block = "This is a normal paragraph of text."
        assert block_to_block_type(block) == BlockType.PARAGRAPH