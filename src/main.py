from textnode import TextNode, TextType, text_node_to_html_node
from htmlnode import HTMLNode, LeafNode, ParentNode

def main():
    #print("Hello world")
    txt_node = TextNode("Hello World", TextType.PLAIN)
    #print(txt_node)
    leaf = text_node_to_html_node(txt_node)
    #print("start")
    #notAFunction("ahha")
    #print("end")
    print(leaf)
    #html_node = HTMLNode("<t>","value",[1,2])
    #print(html_node)




main()