import re

from textnode import TextNode, TextType


def split_nodes_delimiter(old_nodes, delimiter, text_type):
    new_nodes = []
    for old_node in old_nodes:
        if old_node.text_type != TextType.TEXT:
            new_nodes.append(old_node)
            continue
        split_nodes = []
        new_strings = old_node.text.split(delimiter)
        if len(new_strings) % 2 == 0:
            raise ValueError("Invalid markdown, formatted section not closed.")
        for i in range(len(new_strings)):
            if new_strings[i] == "":
                continue
            if i % 2 == 0:
                split_nodes.append(TextNode(new_strings[i], TextType.TEXT))
            else:
                split_nodes.append(TextNode(new_strings[i], text_type))
        new_nodes.extend(split_nodes)
    return new_nodes


def extract_markdown_images(text):
    images = re.findall(
        r"\[(.*?)\]\((https:\/\/(?:\w+\.)*\w+\.\w{1,3}\/\w+\.\w{1,4})\)", text
    )
    return images


def extract_markdown_links(text):
    links = re.findall(
        r"(?<!!)\[(.*?)\]\((https:\/\/(?:\w+\.)*\w+\.\w+\/?(?:.*?)*)\)", text
    )
    return links


def split_nodes_image(old_nodes):
    new_nodes = []
    for old_node in old_nodes:
        strings = []
        original_text = old_node.text
        images = extract_markdown_images(original_text)
        if old_node.text_type != TextType.TEXT or not images:
            new_nodes.append(old_node)
            continue
        for image in images:
            strings = original_text.split(f"![{image[0]}]({image[1]})", 1)
            if strings[0] != "":
                new_nodes.append(TextNode(strings[0], TextType.TEXT))

            new_nodes.append(TextNode(image[0], TextType.IMAGE, image[1]))

            original_text = strings[1]
        if original_text != "":
            new_nodes.append(TextNode(strings[1], TextType.TEXT))

    return new_nodes


def split_nodes_link(old_nodes):
    new_nodes = []
    for old_node in old_nodes:
        strings = []
        original_text = old_node.text
        links = extract_markdown_links(original_text)
        if old_node.text_type != TextType.TEXT or not links:
            new_nodes.append(old_node)
            continue
        for link in links:
            strings = original_text.split(f"[{link[0]}]({link[1]})", 1)
            if strings[0] != "":
                new_nodes.append(TextNode(strings[0], TextType.TEXT))

            new_nodes.append(TextNode(link[0], TextType.LINK, link[1]))

            original_text = strings[1]
        if original_text != "":
            new_nodes.append(TextNode(strings[1], TextType.TEXT))

    return new_nodes


def text_to_textnodes(text):
    new_nodes = [TextNode(text, TextType.TEXT)]
    new_nodes = split_nodes_delimiter(new_nodes, "**", TextType.BOLD)
    new_nodes = split_nodes_delimiter(new_nodes, "*", TextType.ITALIC)
    new_nodes = split_nodes_delimiter(new_nodes, "`", TextType.CODE)
    new_nodes = split_nodes_link(new_nodes)
    new_nodes = split_nodes_image(new_nodes)
    return new_nodes
