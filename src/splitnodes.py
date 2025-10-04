from textnode import TextType, TextNode
from extractmarkdown import extract_markdown_links, extract_markdown_images

def split_nodes_delimiter(old_nodes, delimiter, text_type):
    new_nodes = []
    for old_node in old_nodes:
        if old_node.text_type != TextType.TEXT:
            new_nodes.append(old_node)
            continue        
        splitted = old_node.text.split(delimiter)
        if len(splitted) % 2 == 0:
            raise Exception("invalid markdown syntax, no matching closing delimiter found")
        for i in range(len(splitted)):
            if i % 2 == 0:
                if splitted[i].strip() != "":
                    new_node = TextNode(splitted[i], TextType.TEXT)
                    new_nodes.append(new_node)
            elif i % 2 != 0:
                if splitted[i].strip() == "":
                    raise Exception("empty formatted strings not allowed")
                new_node = TextNode(splitted[i], text_type)
                new_nodes.append(new_node)            
    return new_nodes

def split_nodes_image(old_nodes):
    new_nodes = []
    for old_node in old_nodes:
        if old_node.text_type != TextType.TEXT:
            new_nodes.append(old_node)
            continue

        extracted = extract_markdown_images(old_node.text)
        if not extracted:
            new_nodes.append(old_node)
            continue

        remaining = old_node.text
        for alt, link in extracted:
            delim = f"![{alt}]({link})"
            sections = remaining.split(delim, 1)
            left = sections[0]
            right = sections[1] if len(sections) == 2 else ""

            if left:
                new_nodes.append(TextNode(left, TextType.TEXT))
            new_nodes.append(TextNode(alt, TextType.IMAGE, link))
            remaining = right

        if remaining:
            new_nodes.append(TextNode(remaining, TextType.TEXT))

    return new_nodes
