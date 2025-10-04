from textnode import TextType, TextNode

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
