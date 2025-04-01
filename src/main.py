import os
import shutil

from markdown_to_html import *
from textnode import *
from utils import extract_title


def main():
    text_node = TextNode("This is a text node", TextType.BOLD, "https://www.boot.dev")
    extract_title(
        """# Tolkien Fan Club

**I like Tolkien**. Read my [first post here](/majesty) (sorry the link doesn't work yet)

> All that is gold does not glitter

## Reasons I like Tolkien

* You can spend years studying the legendarium and still not understand its depths
* It can be enjoyed by children and adults alike
* Disney *didn't ruin it*
* It created an entirely new genre of fantasy

## My favorite characters (in order)

1. Gandalf
2. Bilbo
3. Sam
4. Glorfindel
5. Galadriel
6. Elrond
7. Thorin
8. Sauron
9. Aragorn

Here's what `elflang` looks like (the perfect coding language):

```
func main(){
    fmt.Println("Hello, World!")
}
```"""
    )
    copy_contents("static", "public")
    generate_page("content/index.md", "template.html", "public/index.html")


def copy_contents(source, destination):
    if os.path.exists(destination) and destination == "public":
        shutil.rmtree(destination)
    files = os.listdir(source)
    os.mkdir(destination)
    for file in files:
        if os.path.isfile(f"{source}/{file}"):
            dest = shutil.copy(f"{source}/{file}", f"{destination}/{file}")
        else:
            dest = os.path.join(destination, file)
            copy_contents(os.path.join(source, file), dest)


def generate_page(from_path, template_path, dest_path):
    print(f"Generating page from {from_path} to {dest_path} using {template_path}")
    markdown = open(from_path).read()
    template = open(template_path).read()
    html_string = markdown_to_html_node(markdown).to_html()
    title = extract_title(markdown)

    html = template.replace("{{ Title }}", title)
    html = template.replace("{{ Content }}", html_string)

    os.makedirs(dest_path, exist_ok=True)
    with open(dest_path[:-1], "w") as file:
        file.write(html)


if __name__ == "__main__":

    main()
