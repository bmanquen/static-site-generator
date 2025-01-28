from htmlnode import HTMLNode


class ParentNode(HTMLNode):
    def __init__(self, tag, children, props=None):
        self.tag = tag
        self.children = children
        self.props = props

        super().__init__(tag=self.tag, children=self.children, props=self.props)

    def __repr__(self):
        return f"ParentNode({self.tag}, {self.children}, {self.props})"

    def to_html(self):
        if not self.tag:
            raise ValueError("Invalid ParentNode: no tag")
        if not self.children:
            raise ValueError("Invalid ParentNode: no children")

        html_string = f"<{self.tag}{self.props_to_html()}>"
        for child in self.children:
            html_string += child.to_html()
        return html_string + f"</{self.tag}>"
