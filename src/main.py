import os
import shutil
import sys
from pathlib import Path

from markdown_to_html import *
from textnode import *
from utils import extract_title


def main():
    basepath = sys.argv[1] if len(sys.argv) > 1 else "/"
    copy_contents("static", "docs")
    generate_pages_recursive("content", "template.html", "docs", basepath)


def copy_contents(source, destination):
    if os.path.exists(destination) and destination == "docs":
        shutil.rmtree(destination)
    os.mkdir(destination)
    for filename in os.listdir(source):
        from_path = os.path.join(source, filename)
        dest_path = os.path.join(destination, filename)
        if os.path.isfile(from_path):
            shutil.copy(from_path, dest_path)
        else:
            copy_contents(from_path, dest_path)


def generate_page(from_path, template_path, dest_path, basepath):
    markdown = open(from_path).read()
    template = open(template_path).read()
    html_string = markdown_to_html_node(markdown).to_html()
    title = extract_title(markdown)

    template = template.replace("{{ Title }}", title)
    template = template.replace("{{ Content }}", html_string)
    template = template.replace('href="/', f'href="{basepath}')
    template = template.replace('src="/', f'src="{basepath}')

    dest_dirs, file = os.path.split(dest_path)
    dest_path = dest_path.replace(".md", ".html")
    os.makedirs(dest_dirs, exist_ok=True)
    with open(dest_path, "w") as file:
        file.write(template)


def generate_pages_recursive(dir_path_content, template_path, dest_dir_path, basepath):
    files = os.listdir(dir_path_content)
    for file in files:
        if os.path.isfile(f"{dir_path_content}/{file}"):
            generate_page(
                f"{dir_path_content}/{file}",
                template_path,
                f"{dest_dir_path}/{file}",
                basepath,
            )
        else:
            dest = os.path.join(dest_dir_path, file)
            generate_pages_recursive(
                os.path.join(dir_path_content, file), template_path, dest, basepath
            )


if __name__ == "__main__":

    main()
