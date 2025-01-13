class HTMLNode:
    def __init__(self, tag=None, value=None, children=None, props=None):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props

    def to_html(self):
        raise NotImplementedError("to_html method is not implemented")

    def props_to_html(self):
        prop_strings = []
        if not self.props:
            return ""
        for prop_key, prop_value in self.props.items():
            prop_strings.append(f' {prop_key}="{prop_value}"')
        return "".join(prop_strings)

    def __repr__(self):
        return f"HTMLNode({self.tag}, {self.value}, {self.children}, {self.props})"
