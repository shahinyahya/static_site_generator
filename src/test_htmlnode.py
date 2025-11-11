import unittest

from htmlnode import HTMLNode, LeafNode

class TestHTMLNode(unittest.TestCase):
    def test_not_eq(self):
        node1 = HTMLNode(tag="p", value="This is just a paragraph.")
        node2 = HTMLNode(tag="a", value="Links", props={"href": "https://google.com"})
        
        self.assertNotEqual(node1, node2)

    def prop_to_html(self):
        node = HTMLNode("a", "link", props={"href": "https://yandex.com"})
        assert node.props_to_html() == ' href="https://y8.com" target=_blank'

    def test_props_to_html_none(self):
        node = HTMLNode("p", "hello", props=None)
        assert node.props_to_html() == ""

    def test_leaf_to_html_p(self):
        node = LeafNode("p", "Hello, world!")
        self.assertEqual(node.to_html(), "<p>Hello, world!</p>")

    def test_leaf_to_html_h1(self):
        node = LeafNode("h1", "This is heading 1.", props={"class": "head"})
        self.assertEqual(node.to_html(), "<h1 class=\"head\">This is heading 1.</h1>")
        

if __name__ == "__main__":
    unittest.main()
