import re
from textnode import TextNode, TextType

def split_nodes_delimiter(old_nodes, delimiter, text_type):
    new_nodes = []
    for node in old_nodes:
        if node.text_type != TextType.PLAIN:
            new_nodes.append(node)
            continue
        splitted = node.text.split(delimiter)
        #print(splitted)
        if len(splitted)% 2 == 0:
            raise Exception("Something wasn't opened or closed")
        for i in range(len(splitted)):
            if splitted[i] == "":
                continue
            if i%2 == 0:
                new_nodes.append(TextNode(splitted[i], TextType.PLAIN)) #node.text_type
            else:
                new_nodes.append(TextNode(splitted[i], text_type))
    return new_nodes

def extract_markdown_images(text):
    #TIP: r"!\[([^\[\]]*)\]\(([^\(\)]*)\)"
    #raw_data = re.findall(r"!\[(\w+)\]\((.*?)\)",text)
    raw_data = re.findall(r"!\[(.*?)\]\((.*?)\)",text)
    #print(raw_data)
    return raw_data

def extract_markdown_links(text):
    #TIP: r"(?<!!)\[([^\[\]]*)\]\(([^\(\)]*)\)"
    #raw_data = re.findall(r"\[(\w+)\]\((.*?)\)",text)
    raw_data = re.findall(r"\[(.*?)\]\((.*?)\)",text)
    #print(raw_data)
    return raw_data

def split_nodes_image(old_nodes):
    new_nodes= []
    for node in old_nodes:
        if node.text_type != TextType.PLAIN:
            new_nodes.append(node)
            continue
        pointer = 0
        matches = extract_markdown_images(node.text)
        for match in matches:
            length = len(match[0]) + len(match[1]) + 5
            start = node.text.find(match[0]) -2
            end = start + length
            new_nodes.append(TextNode(node.text[pointer:start], TextType.PLAIN))
            new_nodes.append(TextNode(match[0], TextType.IMAGE, match[1]))
            pointer = end
        if len(node.text[pointer:]) > 0:
            new_nodes.append(TextNode(node.text[pointer:], TextType.PLAIN))
    return new_nodes

def split_nodes_link(old_nodes):
    new_nodes= []
    for node in old_nodes:
        if node.text_type != TextType.PLAIN:
            new_nodes.append(node)
            continue
        pointer = 0
        matches = extract_markdown_links(node.text)
        for match in matches:
            length = len(match[0]) + len(match[1]) + 4
            start = node.text.find(match[0]) -1
            end = start + length
            new_nodes.append(TextNode(node.text[pointer:start], TextType.PLAIN))
            new_nodes.append(TextNode(match[0], TextType.LINK, match[1]))
            pointer = end
        if len(node.text[pointer:]) > 0:
            new_nodes.append(TextNode(node.text[pointer:], TextType.PLAIN))
    return new_nodes

def text_to_textnodes(text):
    new_nodes = [TextNode(text, TextType.PLAIN)]
    new_nodes = split_nodes_delimiter(new_nodes, "**", TextType.BOLD)
    new_nodes = split_nodes_delimiter(new_nodes, "_", TextType.ITALIC)
    new_nodes = split_nodes_delimiter(new_nodes, "`", TextType.CODE)
    new_nodes = split_nodes_image(new_nodes)
    new_nodes = split_nodes_link(new_nodes)
    return new_nodes