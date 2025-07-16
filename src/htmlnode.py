class HTMLNode:
    def __init__(self, tag=None, value=None, children=None, props=None):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props
    
    def to_html(self):
        raise NotImplementedError("to_html not implemented")
    
    def props_to_html(self):
        ret_string = ""
        if self.props is None:
            return ret_string
        for prop in self.props:
            ret_string += f' {prop}="{self.props[prop]}"'
        return ret_string
        
    def __repr__(self):
        return f"HTMLNode({self.tag}, {self.value}, children: {self.children}, props: {self.props})"

class LeafNode(HTMLNode):
    def __init__(self, tag, value, props=None):
        super().__init__(tag,value,None,props)
    
    def to_html(self):
        ret_string = ""
        if self.value == None:
            raise ValueError("All leafnodes must have a value")
        if self.tag == None:
            return self.value
        ret_string = f"<{self.tag}{self.props_to_html()}>{self.value}</{self.tag}>"
        return ret_string
    
    def __repr__(self):
        return f"LeafNode({self.tag}, {self.value}, props: {self.props})"

class ParentNode(HTMLNode):
    def __init__(self, tag, children, props=None):
        super().__init__(tag,None,children,props)
        
    
    def to_html(self):
        if self.tag == None:
            raise ValueError("All ParentNodes must have a tag")
        if self.children == None:
            raise ValueError("All ParentNodes must have children")
        ret_string = f"<{self.tag}>"
        for child in self.children:
            ret_string += child.to_html()
        ret_string += f"</{self.tag}>"
        return ret_string
    
    def __repr__(self):
        return f"ParentNode({self.tag}, Children: {self.children}, props: {self.props})"