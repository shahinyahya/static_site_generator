import unittest

from leafnode import LeafNode

class TestLeafNode(unittest.TestCase):
    def test_leaf_to_html_p(self):
        node = LeafNode("p", "Hello, world!")
        self.assertEqual(node.to_html(), "<p>Hello, world!</p>")

    def test_leaf_to_html_h1(self):
        node = LeafNode("h1", "This is heading 1.", props={"class": "head"})
        self.assertEqual(node.to_html(), "<h1 class=\"head\">This is heading 1.</h1>")

if __name__ == "__main__":
    unittest.main()