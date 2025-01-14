from textnode import TextNode, TextType


def split_nodes_delimiter(old_nodes, delimiter, text_type):
    new_nodes = []
    for old_node in old_nodes:
        if old_node.text_type != TextType.TEXT:
            new_nodes.append(old_node)
            continue
        new_strings = old_node.text.split(delimiter)
        if len(new_strings) % 2 == 0:
            raise ValueError("Invalid markdown, formatted section not closed.")
        for i in range(len(new_strings)):
            if i % 2 == 0:
                new_strings[i] = TextNode(new_strings[i], TextType.TEXT)
            else:
                new_strings[i] = TextNode(new_strings[i], text_type)
        new_nodes.extend(new_strings)
    return new_nodes
