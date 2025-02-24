import os
import shutil

from textnode import *


def main():
    text_node = TextNode("This is a text node", TextType.BOLD, "https://www.boot.dev")
    copy_contents("static", "public")


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


if __name__ == "__main__":
    main()
