import unittest

from extract_markdown_html import extract_title

class TestExtractMarkdownToHTML(unittest.TestCase):
    def test_extract_basic(self):
        assert extract_title("# Hello") == "Hello"
    
    def test_extract_spaces(self):
        assert extract_title("#     Title   ") == "Title"

    def test_title_no_space_after_hash(self):
        assert extract_title("#Title") == "Title"