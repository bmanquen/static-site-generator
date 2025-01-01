class HTMLNode():
    def __init__(self, tag = None, value = None, children = None, props = None):
        self.tag = tag 
        self.value = value
        self.children = children
        self.props = props

    def to_html(self):
        raise NotImplementedError

    def props_to_html(self):
        prop_strings = []
        if self.props:
            for prop_key, prop_value in self.props.items():
                prop_strings.append(f' {prop_key}="{prop_value}"')
            return "".join(prop_strings)
        return ""

    def __repr__(self):
        children_list = []
        if self.children:
            for child in self.children:
                children_list.append(f"HTMLNode({child.tag}, {child.value}, {child.children}, {child.props})")
        return f"HTMLNode({self.tag}, {self.value}, {children_list}, {self.props})"

