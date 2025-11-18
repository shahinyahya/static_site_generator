import unittest

from src.splitnode import split_nodes_delimiter
from src. textnode import TextType, TextNode

class TestSplitNode(unittest.TestCase):

    def test_split_node_delimitter(self):
        node = TextNode("This is text with a code `code block` and a word", TextType.TEXT)
        result = split_nodes_delimiter([node], "`", TextType.CODE)

        assert len(result) == 3
        assert result[0].text == "This is text with a code "
        assert result[0].text_type == TextType.TEXT
        assert result[1].text == "code block"
        assert result[1].text_type == TextType.CODE
        assert result[2].text == " and a word"
        assert result[2].text_type == TextType.TEXT