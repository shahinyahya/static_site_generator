from markdown_function import markdown_to_blocks, block_to_block_type, BlockType
from htmlnode import HTMLNode
from functions import text_to_textnodes, text_node_to_html_node
from parentnode import ParentNode
from leafnode import LeafNode

def markdown_to_html_node(markdown):
    
    # Create parent node
    # parent_node = HTMLNode('div')

    # Split markdown to blocks
    blocks = markdown_to_blocks(markdown)
    children = []

    for block in blocks:
        
        # Determine block type
        block_type = block_to_block_type(block)

        # Check for block tags
        
        ## HEADING
        if block_type == BlockType.HEADING:
            # create HTML block heading 1 through 6
            level = len(block.split(" ")[0]) #split #
            text = block[level:].strip()

            textnodes = text_to_textnodes(text)
            inline_children = [text_node_to_html_node(n) for n in textnodes]

            children.append(ParentNode(f"h{level}", inline_children))
            continue

        ## PARAGRAPH
        if block_type == BlockType.PARAGRAPH:
            # create HTML block for paragraph.
            text = " ".join(block.splitlines())
            textnodes = text_to_textnodes(text)
            inline_children = [text_node_to_html_node(n) for n in textnodes]

            children.append(ParentNode("p", inline_children))
            continue

        ## QUOTE
        if block_type == BlockType.QUOTE:
            # Create HTML block for quotes
            cleaned = "\n".join(line[1:].strip() for line in block.split("\n"))            

            textnodes = text_to_textnodes(cleaned)
            inline_children = [text_node_to_html_node(n) for n in textnodes]

            children.append(ParentNode("blockquote", inline_children))
            continue

        ## UNORDERED LIST
        if block_type == BlockType.UNORDERED_LIST:
            li_nodes = []
            for line in block.split("\n"):
                item_text = line[1:].strip()
                textnodes = text_to_textnodes(item_text)
                inline_children = [text_node_to_html_node(n) for n in textnodes]

                # append list in li tag
                li_nodes.append(ParentNode("li", inline_children))

            children.append(ParentNode("ul", li_nodes))
            continue

        ## ORDERED LIST
        if block_type == BlockType.ORDERED_LIST:
            li_nodes = []
            for line in block.split("\n"):
                item_text = line.split(". ", 1)[1]
                textnodes = text_to_textnodes(item_text)
                inline_children = [text_node_to_html_node(n) for n in textnodes]

                # append list in li tag
                li_nodes.append(ParentNode("li", inline_children))

            children.append(ParentNode("ol", li_nodes))
            continue

        ## CODE
        if block_type == BlockType.CODE:
            lines = block.split("\n")
            lang = lines[0][3:].strip()
            inner = "\n".join(lines[1:-1])

            code_leaf = LeafNode("code", inner)

            if lang:
                code_leaf.props = {"class": f"language-{lang}"}

            pre = ParentNode("pre", [code_leaf])
            children.append(pre)
            continue
    
    return ParentNode("div", children)

