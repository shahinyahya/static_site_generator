import unittest

from extractnode import extract_markdown_images, extract_markdown_links

class TestExtractNode(unittest.TestCase):
    def test_extract_markdown_images(self):
        matches = extract_markdown_images(
            "This is text with an ![image](https://i.imgur.com/zjjcJKZ.png)"
        )
        self.assertListEqual([("image", "https://i.imgur.com/zjjcJKZ.png")], matches)
    
    def test_extract_multiple_images(self):
        text = "![a](url1) text ![b](url2)"
        self.assertListEqual(
             [("a", "url1"), ("b", "url2")],
            extract_markdown_images(text)
        )

    def test_extract_markdown_links(self):
        matches = extract_markdown_links(
            "A link to [Google](https://google.com)"
        )
        self.assertListEqual(
            [("Google", "https://google.com")],
            matches
        )

    def test_link_not_image(self):
        matches = extract_markdown_links(
            "![img](url1) and [real link](url2)"
        )
        self.assertListEqual(
            [("real link", "url2")],
            matches
        )

    def test_multiple_links(self):
        text = "[a](u1) and [b](u2)"
        self.assertListEqual(
            [("a", "u1"), ("b", "u2")],
            extract_markdown_links(text)
        )