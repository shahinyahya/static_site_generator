import unittest

from src.splitnode import split_nodes_delimiter, split_nodes_image, split_nodes_link
from src. textnode import TextType, TextNode
from src.functions import text_to_textnodes

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

    def test_split_nodes_images(self):
        node = TextNode("This is text with an ![image](https://i.imgur.com/zjjcJKZ.png) and another ![second image](https://i.imgur.com/3elNhQu.png)",TextType.TEXT)
        new_nodes = split_nodes_image([node])
        self.assertListEqual(
            [
                TextNode("This is text with an ", TextType.TEXT),
                TextNode("image", TextType.IMAGE, "https://i.imgur.com/zjjcJKZ.png"),
                TextNode(" and another ", TextType.TEXT),
                TextNode("second image", TextType.IMAGE, "https://i.imgur.com/3elNhQu.png"),
            ],
            new_nodes,
        )
    
    def test_split_nodes_image(self):
        node = TextNode("My favorite website is [OpenAI](https://openai.com) because it has great AI tools.", TextType.TEXT)
        new_nodes = split_nodes_link([node])
        self.assertListEqual(
            [
                TextNode("My favorite website is ", TextType.TEXT),
                TextNode("OpenAI", TextType.LINK, "https://openai.com"),
                TextNode(" because it has great AI tools.", TextType.TEXT)
            ],
            new_nodes
        )

    def test_text_to_textnodes_full_example(self):
        text = (
            "This is **text** with an _italic_ word and a `code block` and an "
            "![obi wan image](https://i.imgur.com/fJRm4Vk.jpeg) and a "
            "[link](https://boot.dev)"
        )

        result = text_to_textnodes(text)

        assert result == [
            TextNode("This is ", TextType.TEXT),
            TextNode("text", TextType.BOLD),
            TextNode(" with an ", TextType.TEXT),
            TextNode("italic", TextType.ITALIC),
            TextNode(" word and a ", TextType.TEXT),
            TextNode("code block", TextType.CODE),
            TextNode(" and an ", TextType.TEXT),
            TextNode("obi wan image", TextType.IMAGE, "https://i.imgur.com/fJRm4Vk.jpeg"),
            TextNode(" and a ", TextType.TEXT),
            TextNode("link", TextType.LINK, "https://boot.dev"),
        ]
