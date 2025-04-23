import os
import shutil
from pathlib import Path

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
    generate_pages_recursive("content", "template.html", "public")


def copy_contents(source, destination):
    if os.path.exists(destination) and destination == "public":
        shutil.rmtree(destination)
    os.mkdir(destination)
    for filename in os.listdir(source):
        from_path = os.path.join(source, filename)
        dest_path = os.path.join(destination, filename)
        if os.path.isfile(from_path):
            shutil.copy(from_path, dest_path)
        else:
            copy_contents(from_path, dest_path)


def generate_page(from_path, template_path, dest_path):
    markdown = open(from_path).read()
    template = open(template_path).read()
    html_string = markdown_to_html_node(markdown).to_html()
    title = extract_title(markdown)

    template = template.replace("{{ Title }}", title)
    template = template.replace("{{ Content }}", html_string)

    dest_dirs, file = os.path.split(dest_path)
    dest_path = dest_path.replace(".md", ".html")
    os.makedirs(dest_dirs, exist_ok=True)
    with open(dest_path, "w") as file:
        file.write(template)


def generate_pages_recursive(dir_path_content, template_path, dest_dir_path):
    files = os.listdir(dir_path_content)
    for file in files:
        if os.path.isfile(f"{dir_path_content}/{file}"):
            generate_page(
                f"{dir_path_content}/{file}", template_path, f"{dest_dir_path}/{file}"
            )
        else:
            dest = os.path.join(dest_dir_path, file)
            generate_pages_recursive(
                os.path.join(dir_path_content, file), template_path, dest
            )


if __name__ == "__main__":

    main()
