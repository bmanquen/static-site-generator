import re


def markdown_to_blocks(markdown):
    block_strings = []
    strings = markdown.split("\n\n")
    for string in strings:
        if string.strip() != "":
            block_strings.append(string.strip())
    return block_strings


def block_to_block_type(block):
    match block:
        case _ if re.match(r"^\#{1,6}\s+.*", block):
            return "heading"
        case _ if re.match(r"^```.*```$", block):
            return "code"
        case _ if re.match(r"^(?:>.*\n*)+", block):
            return "quote"
        case _ if re.match(r"^(?:[\*\-]\s+.*\n*)+", block):
            return "unordered list"
        case _ if re.match(r"^(?:\d+\..*\n*)+", block):
            return "ordered list"
        case _:
            return "paragraph"
