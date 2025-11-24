import unittest

from textnode import TextNode, TextType

class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is test node 1", TextType.BOLD)
        node2 = TextNode("This is test node 2", TextType.ITALIC)
    
        node3 = TextNode("img_text", TextType.IMAGE, "qwerty")
        node4 = TextNode("link", TextType.LINK, "ytrewq")

        # self.assertEqual(node, node2)
        # self.assertNotEqual(node, node2)
        # self.assertNotEqual(node3, node4)


if __name__ == "__main__":
    unittest.main()
