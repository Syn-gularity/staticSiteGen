from textnode import TextNode, TextType, text_node_to_html_node
from htmlnode import HTMLNode, LeafNode, ParentNode
from markdown import split_nodes_delimiter, extract_markdown_images, split_nodes_image, text_to_textnodes

def main():
    #print("Hello world")
    #txt_node = TextNode("Hello World", TextType.PLAIN)
    #print(txt_node)
    #leaf = text_node_to_html_node(txt_node)
    #print("start")
    #notAFunction("ahha")
    #print("end")
    #print(leaf)
    #html_node = HTMLNode("<t>","value",[1,2])
    #print(html_node)
    #matches = extract_markdown_images(
    #        "This is text with an ![image](https://i.imgur.com/zjjcJKZ.png)"
    #    )
    #print(matches)
    #
    #node = TextNode(
    #        "This is text with an ![image](https://i.imgur.com/zjjcJKZ.png) and another ![second image](https://i.imgur.com/3elNhQu.png)",
    #        TextType.PLAIN,
    #    )
    #new_nodes = split_nodes_image([node])
    #print(new_nodes)
    string = "This is **text** with an _italic_ word and a `code block` and an ![obi wan image](https://i.imgur.com/fJRm4Vk.jpeg) and a [link](https://boot.dev)"
    new_nodes = [TextNode(string, TextType.PLAIN)]
    new_nodes = split_nodes_delimiter(new_nodes, "**", TextType.BOLD)
    new_nodes = split_nodes_delimiter(new_nodes, "_", TextType.ITALIC)
    print(new_nodes)
    nodes = text_to_textnodes(
            "This is **text** with an _italic_ word and a `code block` and an ![image](https://i.imgur.com/zjjcJKZ.png) and a [link](https://boot.dev)"
        )
    print(nodes)




main()