from htmlnode import HTMLNode


class LeafNode(HTMLNode):
    def __init__(self, tag, value, props=None):
        self.tag = tag
        self.value = value
        self.props = props

        super().__init__(tag=self.tag, value=self.value, props=self.props)

    def to_html(self):
        if not self.value:
            raise ValueError("Invalid LeafNode: no value")
        if not self.tag:
            return self.value
        return f"<{self.tag}{self.props_to_html()}>{self.value}</{self.tag}>"
