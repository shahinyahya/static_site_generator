from enum import Enum
import re

class BlockType(Enum):
    PARAGRAPH = "paragraph"
    HEADING = "heading"
    CODE = "code"
    QUOTE = "quote"
    UNORDERED_LIST = "unordered_list"
    ORDERED_LIST = "ordered_list"

def markdown_to_blocks(markdown):
    
    # Split double new line
    raw_blocks = re.split(r"\n\s*\n", markdown)

    blocks = []
    for block in raw_blocks:
        cleaned = block.strip()
        if cleaned:
            blocks.append(cleaned)
        
    return blocks

def block_to_block_type(block):
    
    lines = block.split("\n")

    # Code Block
    # starts with ``` and ```
    if lines[0].startswith("```") and lines[-1].startswith("```"):
        return BlockType.CODE
    
    # Heading fom 1 to 6
    if re.match(r"^#{1,6} .+", lines[0]):
        return BlockType.HEADING

    # Quote Block starts with >
    if all(line.startswith(">") for line in lines):
        return BlockType.QUOTE
    
    # Unordered List Block
    if all(line.startswith("-") for line in lines):
        return BlockType.UNORDERED_LIST
    
    # Ordered List Block
    ordered_list_match = True
    # Increment the number 1 to n
    for index, line in enumerate(lines, start=1):
        if not re.match(rf"^{index}\. .+", line):
            ordered_list_match = False
            break
    if ordered_list_match:
        return BlockType.ORDERED_LIST
    
    return BlockType.PARAGRAPH
