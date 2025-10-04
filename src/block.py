import enum

class BlockType(enum):
    PARAGRAPH = "paragraph"
    HEADING = "heading"
    CODE = "code"
    QUOTE = "quote"
    UNORDERED_LIST = "unordered_list"
    ORDERED_LIST = "ordered_list"

def block_to_block_type(block):
    if block.startswith("#"):
        splitted = block.split(" ", 1)
        count = splitted[0].count("#")
        if  count >= 1 and count <= 6:
            return BlockType.HEADING
    elif block.startswith("```") and block.endswith("```"):
        return BlockType.CODE
    block_lines = block.split("\n")
    for line in block_lines:
        if line.startswith(">"):
            continue
        else:
            
        
    else:
        return BlockType.PARAGRAPH